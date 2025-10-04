"""
Asynchronous proxy registration with heartbeat functionality.

This module provides automatic proxy registration in a separate thread
with continuous heartbeat monitoring and automatic re-registration on failures.

Author: Vasiliy Zdanovskiy
email: vasilyvz@gmail.com
"""

import asyncio
import time
import threading
from typing import Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum

from mcp_proxy_adapter.core.logging import logger
from mcp_proxy_adapter.core.proxy_registration import ProxyRegistrationManager


class RegistrationState(Enum):
    """Registration state enumeration."""
    DISABLED = "disabled"
    NOT_REGISTERED = "not_registered"
    REGISTERING = "registering"
    REGISTERED = "registered"
    HEARTBEAT_FAILED = "heartbeat_failed"
    ERROR = "error"


@dataclass
class RegistrationStatus:
    """Registration status information."""
    state: RegistrationState
    server_key: Optional[str] = None
    last_attempt: Optional[float] = None
    last_success: Optional[float] = None
    last_error: Optional[str] = None
    attempt_count: int = 0
    success_count: int = 0


class AsyncProxyRegistrationManager:
    """
    Asynchronous proxy registration manager with heartbeat functionality.
    
    Runs registration and heartbeat in a separate thread, automatically
    handling re-registration on failures and continuous monitoring.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the async proxy registration manager.
        
        Args:
            config: Application configuration
        """
        self.config = config
        self.registration_manager = ProxyRegistrationManager(config)
        self.status = RegistrationStatus(state=RegistrationState.NOT_REGISTERED)
        self._thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        
        # Get heartbeat configuration
        heartbeat_config = config.get("registration", {}).get("heartbeat", {})
        self.heartbeat_enabled = heartbeat_config.get("enabled", True)
        self.heartbeat_interval = heartbeat_config.get("interval", 30)
        self.heartbeat_timeout = heartbeat_config.get("timeout", 10)
        self.retry_attempts = heartbeat_config.get("retry_attempts", 3)
        self.retry_delay = heartbeat_config.get("retry_delay", 5)
        
        logger.info(f"AsyncProxyRegistrationManager initialized: heartbeat_enabled={self.heartbeat_enabled}, interval={self.heartbeat_interval}s")
    
    def is_enabled(self) -> bool:
        """Check if proxy registration is enabled."""
        return self.registration_manager.is_enabled()
    
    def set_server_url(self, server_url: str):
        """Set the server URL for registration."""
        self.registration_manager.set_server_url(server_url)
        logger.info(f"Server URL set for async registration: {server_url}")
    
    def start(self):
        """Start the async registration and heartbeat thread."""
        if not self.is_enabled():
            logger.info("Proxy registration is disabled, not starting async manager")
            self.status.state = RegistrationState.DISABLED
            return
        
        if self._thread and self._thread.is_alive():
            logger.warning("Async registration thread is already running")
            return
        
        logger.info("Starting async proxy registration and heartbeat thread")
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run_async_loop, daemon=True)
        self._thread.start()
    
    def stop(self):
        """Stop the async registration and heartbeat thread."""
        if not self._thread or not self._thread.is_alive():
            return
        
        logger.info("Stopping async proxy registration and heartbeat thread")
        self._stop_event.set()
        
        # Unregister if registered
        if self.status.state == RegistrationState.REGISTERED:
            try:
                # Run unregistration in the thread's event loop
                if self._loop and not self._loop.is_closed():
                    future = asyncio.run_coroutine_threadsafe(
                        self.registration_manager.unregister_server(), 
                        self._loop
                    )
                    future.result(timeout=10)
                    logger.info("Successfully unregistered from proxy during shutdown")
            except Exception as e:
                logger.error(f"Failed to unregister during shutdown: {e}")
        
        self._thread.join(timeout=5)
        if self._thread.is_alive():
            logger.warning("Async registration thread did not stop gracefully")
    
    def _run_async_loop(self):
        """Run the async event loop in the thread."""
        try:
            self._loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self._loop)
            self._loop.run_until_complete(self._async_main())
        except Exception as e:
            logger.error(f"Async registration loop error: {e}")
        finally:
            if self._loop and not self._loop.is_closed():
                self._loop.close()
    
    async def _async_main(self):
        """Main async loop for registration and heartbeat."""
        logger.info("Async registration loop started")
        
        # Initial registration attempt
        await self._attempt_registration()
        
        # Main loop
        while not self._stop_event.is_set():
            try:
                if self.status.state == RegistrationState.REGISTERED:
                    if self.heartbeat_enabled:
                        # Perform heartbeat
                        await self._perform_heartbeat()
                    else:
                        # Just wait if heartbeat is disabled
                        await asyncio.sleep(self.heartbeat_interval)
                else:
                    # Try to register
                    await self._attempt_registration()
                    # Wait before retry
                    await asyncio.sleep(self.retry_delay)
                    
            except Exception as e:
                logger.error(f"Error in async registration loop: {e}")
                self.status.state = RegistrationState.ERROR
                self.status.last_error = str(e)
                await asyncio.sleep(self.retry_delay)
        
        logger.info("Async registration loop stopped")
    
    async def _attempt_registration(self):
        """Attempt to register with the proxy."""
        if self.status.state == RegistrationState.REGISTERING:
            return  # Already registering
        
        self.status.state = RegistrationState.REGISTERING
        self.status.attempt_count += 1
        self.status.last_attempt = time.time()
        
        logger.info(f"Attempting proxy registration (attempt #{self.status.attempt_count})")
        
        try:
            success = await self.registration_manager.register_server()
            
            if success:
                self.status.state = RegistrationState.REGISTERED
                self.status.last_success = time.time()
                self.status.success_count += 1
                self.status.last_error = None
                logger.info(f"✅ Proxy registration successful (attempt #{self.status.attempt_count})")
            else:
                self.status.state = RegistrationState.NOT_REGISTERED
                self.status.last_error = "Registration returned False"
                logger.warning(f"❌ Proxy registration failed (attempt #{self.status.attempt_count}): Registration returned False")
                
        except Exception as e:
            self.status.state = RegistrationState.NOT_REGISTERED
            self.status.last_error = str(e)
            logger.error(f"❌ Proxy registration failed (attempt #{self.status.attempt_count}): {e}")
    
    async def _perform_heartbeat(self):
        """Perform heartbeat to the proxy."""
        try:
            # Use the registration manager's heartbeat functionality
            success = await self.registration_manager.heartbeat()
            
            if success:
                logger.debug("💓 Heartbeat successful")
                self.status.last_success = time.time()
            else:
                logger.warning("💓 Heartbeat failed")
                self.status.state = RegistrationState.HEARTBEAT_FAILED
                self.status.last_error = "Heartbeat failed"
                
                # Try to re-register after heartbeat failure
                logger.info("Attempting re-registration after heartbeat failure")
                await self._attempt_registration()
                
        except Exception as e:
            logger.error(f"💓 Heartbeat error: {e}")
            self.status.state = RegistrationState.HEARTBEAT_FAILED
            self.status.last_error = str(e)
            
            # Try to re-register after heartbeat error
            logger.info("Attempting re-registration after heartbeat error")
            await self._attempt_registration()
        
        # Wait for next heartbeat
        await asyncio.sleep(self.heartbeat_interval)
    
    def get_status(self) -> Dict[str, Any]:
        """Get current registration status."""
        return {
            "state": self.status.state.value,
            "server_key": self.status.server_key,
            "last_attempt": self.status.last_attempt,
            "last_success": self.status.last_success,
            "last_error": self.status.last_error,
            "attempt_count": self.status.attempt_count,
            "success_count": self.status.success_count,
            "heartbeat_enabled": self.heartbeat_enabled,
            "heartbeat_interval": self.heartbeat_interval,
            "thread_alive": self._thread.is_alive() if self._thread else False
        }


# Global instance
_async_registration_manager: Optional[AsyncProxyRegistrationManager] = None


def get_async_registration_manager() -> Optional[AsyncProxyRegistrationManager]:
    """Get the global async registration manager instance."""
    return _async_registration_manager


def initialize_async_registration(config: Dict[str, Any]) -> AsyncProxyRegistrationManager:
    """Initialize the global async registration manager."""
    global _async_registration_manager
    _async_registration_manager = AsyncProxyRegistrationManager(config)
    return _async_registration_manager


def start_async_registration(server_url: str):
    """Start async registration with the given server URL."""
    global _async_registration_manager
    if _async_registration_manager:
        _async_registration_manager.set_server_url(server_url)
        _async_registration_manager.start()
    else:
        logger.error("Async registration manager not initialized")


def stop_async_registration():
    """Stop async registration."""
    global _async_registration_manager
    if _async_registration_manager:
        _async_registration_manager.stop()


def get_registration_status() -> Dict[str, Any]:
    """Get current registration status."""
    global _async_registration_manager
    if _async_registration_manager:
        return _async_registration_manager.get_status()
    else:
        return {"state": "not_initialized"}
