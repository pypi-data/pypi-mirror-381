#!/usr/bin/env python3
"""
Simplified Configuration Builder for MCP Proxy Adapter

Author: Vasiliy Zdanovskiy
email: vasilyvz@gmail.com
"""

import json
import uuid
from enum import Enum
from typing import Dict, List, Optional, Any


class Protocol(Enum):
    """Supported protocols."""
    HTTP = "http"
    HTTPS = "https"
    MTLS = "mtls"


class AuthMethod(Enum):
    """Authentication methods."""
    NONE = "none"
    TOKEN = "token"
    TOKEN_ROLES = "token_roles"


class ConfigBuilder:
    """Simplified configuration builder."""
    
    def __init__(self):
        """Initialize the configuration builder."""
        self._reset_to_defaults()
    
    def _reset_to_defaults(self):
        """Reset configuration to default values."""
        self.config = {
            "uuid": str(uuid.uuid4()),
            "server": {
                "host": "0.0.0.0",
                "port": 8000,
                "protocol": "http",
                "debug": False,
                "log_level": "INFO"
            },
            "logging": {
                "level": "INFO",
                "file": None,
                "log_dir": "./logs",
                "log_file": "mcp_proxy_adapter.log",
                "max_size": 10,
                "backup_count": 5,
                "console_output": True,
                "json_format": False
            },
            "security": {
                "enabled": False,
                "tokens": {
                    "admin": "admin-secret-key",
                    "user": "user-secret-key",
                    "readonly": "readonly-secret-key"
                },
                "roles": {
                    "admin": ["read", "write", "delete", "admin"],
                    "user": ["read", "write"],
                    "readonly": ["read"]
                },
                "roles_file": None
            },
            "debug": {
                "enabled": False,
                "log_level": "DEBUG",
                "trace_requests": False,
                "trace_responses": False
            },
            "transport": {
                "type": "http",
                "port": None,
                "verify_client": False,
                "chk_hostname": False
            },
            "registration": {
                "enabled": False,
                "proxy_url": "http://localhost:3004",
                "public_host": None,  # Auto-determined from hostname or server.host
                "public_port": None,  # Auto-determined from server.port
                "protocol": None,     # Auto-determined from server.protocol
                "server_id": "mcp_proxy_adapter",
                "server_name": "MCP Proxy Adapter",
                "description": "JSON-RPC API for interacting with MCP Proxy",
                "version": "6.6.9",
                "heartbeat": {
                    "enabled": True,
                    "interval": 30,
                    "timeout": 10,
                    "retry_attempts": 3,
                    "retry_delay": 5
                }
            }
        }
    
    def set_protocol(self, protocol: Protocol, cert_dir: str = "./certs", key_dir: str = "./keys"):
        """Set protocol configuration (HTTP, HTTPS, or mTLS)."""
        self.config["server"]["protocol"] = protocol.value
        
        # Set registration protocol to match server protocol
        self.config["registration"]["protocol"] = protocol.value
        
        if protocol == Protocol.HTTP:
            # HTTP - no SSL, no client verification
            self.config["transport"]["verify_client"] = False
            self.config["transport"]["chk_hostname"] = False
            
        elif protocol == Protocol.HTTPS:
            # HTTPS - SSL enabled, no client verification
            self.config["transport"]["verify_client"] = False
            self.config["transport"]["chk_hostname"] = True
            
        elif protocol == Protocol.MTLS:
            # mTLS - SSL enabled, client verification required
            self.config["transport"]["verify_client"] = True
            self.config["transport"]["chk_hostname"] = True
        
        return self
    
    def set_auth(self, auth_method: AuthMethod, api_keys: Optional[Dict[str, str]] = None, roles: Optional[Dict[str, List[str]]] = None):
        """Set authentication configuration."""
        if auth_method == AuthMethod.NONE:
            self.config["security"]["enabled"] = False
            self.config["security"]["tokens"] = {}
            self.config["security"]["roles"] = {}
            self.config["security"]["roles_file"] = None
            
        elif auth_method == AuthMethod.TOKEN:
            self.config["security"]["enabled"] = True
            self.config["security"]["tokens"] = api_keys or {
                "admin": "admin-secret-key",
                "user": "user-secret-key"
            }
            self.config["security"]["roles"] = roles or {
                "admin": ["read", "write", "delete", "admin"],
                "user": ["read", "write"]
            }
            self.config["security"]["roles_file"] = None
            
        elif auth_method == AuthMethod.TOKEN_ROLES:
            self.config["security"]["enabled"] = True
            self.config["security"]["tokens"] = api_keys or {
                "admin": "admin-secret-key",
                "user": "user-secret-key",
                "readonly": "readonly-secret-key"
            }
            self.config["security"]["roles"] = roles or {
                "admin": ["read", "write", "delete", "admin"],
                "user": ["read", "write"],
                "readonly": ["read"]
            }
            self.config["security"]["roles_file"] = "configs/roles.json"
        
        return self
    
    def set_server(self, host: str = "0.0.0.0", port: int = 8000):
        """Set server configuration."""
        self.config["server"]["host"] = host
        self.config["server"]["port"] = port
        return self
    
    def set_roles_file(self, roles_file: str):
        """Set roles file path."""
        self.config["security"]["roles_file"] = roles_file
        return self
    
    def set_proxy_registration(self, enabled: bool = True, proxy_url: str = "http://localhost:3004", 
                               public_host: Optional[str] = None, public_port: Optional[int] = None,
                               server_id: str = "mcp_proxy_adapter", server_name: str = "MCP Proxy Adapter",
                               description: str = "JSON-RPC API for interacting with MCP Proxy"):
        """Set proxy registration configuration."""
        self.config["registration"]["enabled"] = enabled
        self.config["registration"]["proxy_url"] = proxy_url
        self.config["registration"]["public_host"] = public_host
        self.config["registration"]["public_port"] = public_port
        self.config["registration"]["server_id"] = server_id
        self.config["registration"]["server_name"] = server_name
        self.config["registration"]["description"] = description
        
        # Set protocol to match server protocol if not explicitly set
        if self.config["registration"]["protocol"] is None:
            self.config["registration"]["protocol"] = self.config["server"]["protocol"]
        
        return self
    
    def enable_auto_registration(self, proxy_url: str = "http://localhost:3004", 
                                server_id: str = "mcp_proxy_adapter", 
                                server_name: str = "MCP Proxy Adapter",
                                description: str = "JSON-RPC API for interacting with MCP Proxy"):
        """
        Enable automatic proxy registration with auto-determined parameters.
        
        This method enables registration with automatic determination of:
        - public_host: from hostname (if server.host is 0.0.0.0/127.0.0.1) or server.host
        - public_port: from server.port
        - protocol: from server.protocol
        
        Args:
            proxy_url: URL of the proxy server
            server_id: Unique identifier for this server
            server_name: Human-readable name for this server
            description: Description of this server
        """
        self.config["registration"]["enabled"] = True
        self.config["registration"]["proxy_url"] = proxy_url
        self.config["registration"]["public_host"] = None  # Auto-determined
        self.config["registration"]["public_port"] = None  # Auto-determined
        self.config["registration"]["protocol"] = None     # Auto-determined
        self.config["registration"]["server_id"] = server_id
        self.config["registration"]["server_name"] = server_name
        self.config["registration"]["description"] = description
        
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build and return the configuration."""
        return self.config.copy()
    
    def save(self, file_path: str) -> None:
        """Save configuration to file."""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)


class ConfigFactory:
    """Factory for creating common configurations."""
    
    @staticmethod
    def create_http_config(port: int = 8000) -> Dict[str, Any]:
        """Create HTTP configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTP)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_http_token_config(port: int = 8001) -> Dict[str, Any]:
        """Create HTTP with token authentication configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTP)
                .set_auth(AuthMethod.TOKEN)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_http_token_roles_config(port: int = 8002) -> Dict[str, Any]:
        """Create HTTP with token and roles configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTP)
                .set_auth(AuthMethod.TOKEN_ROLES)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_https_config(port: int = 8003) -> Dict[str, Any]:
        """Create HTTPS configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTPS)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_https_token_config(port: int = 8004) -> Dict[str, Any]:
        """Create HTTPS with token authentication configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTPS)
                .set_auth(AuthMethod.TOKEN)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_https_token_roles_config(port: int = 8005) -> Dict[str, Any]:
        """Create HTTPS with token and roles configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTPS)
                .set_auth(AuthMethod.TOKEN_ROLES)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_mtls_config(port: int = 8006) -> Dict[str, Any]:
        """Create mTLS configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.MTLS)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_mtls_token_config(port: int = 8007) -> Dict[str, Any]:
        """Create mTLS with token authentication configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.MTLS)
                .set_auth(AuthMethod.TOKEN)
                .set_server(port=port)
                .build())

    @staticmethod
    def create_mtls_token_roles_config(port: int = 8008) -> Dict[str, Any]:
        """Create mTLS with token and roles configuration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.MTLS)
                .set_auth(AuthMethod.TOKEN_ROLES)
                .set_server(port=port)
                .build())
    
    @staticmethod
    def create_http_with_proxy_config(port: int = 8009, proxy_url: str = "http://localhost:3004") -> Dict[str, Any]:
        """Create HTTP configuration with proxy registration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTP)
                .set_server(port=port)
                .set_proxy_registration(proxy_url=proxy_url)
                .build())
    
    @staticmethod
    def create_https_with_proxy_config(port: int = 8010, proxy_url: str = "https://localhost:3004") -> Dict[str, Any]:
        """Create HTTPS configuration with proxy registration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTPS)
                .set_server(port=port)
                .set_proxy_registration(proxy_url=proxy_url)
                .build())
    
    @staticmethod
    def create_mtls_with_proxy_config(port: int = 8011, proxy_url: str = "https://localhost:3004") -> Dict[str, Any]:
        """Create mTLS configuration with proxy registration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.MTLS)
                .set_server(port=port)
                .set_proxy_registration(proxy_url=proxy_url)
                .build())
    
    @staticmethod
    def create_http_with_auto_registration(port: int = 8009, proxy_url: str = "http://localhost:3004", 
                                         server_id: str = "mcp_proxy_adapter") -> Dict[str, Any]:
        """Create HTTP configuration with automatic proxy registration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTP)
                .set_server(port=port)
                .enable_auto_registration(proxy_url=proxy_url, server_id=server_id)
                .build())
    
    @staticmethod
    def create_https_with_auto_registration(port: int = 8010, proxy_url: str = "https://localhost:3004", 
                                          server_id: str = "mcp_proxy_adapter") -> Dict[str, Any]:
        """Create HTTPS configuration with automatic proxy registration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.HTTPS)
                .set_server(port=port)
                .enable_auto_registration(proxy_url=proxy_url, server_id=server_id)
                .build())
    
    @staticmethod
    def create_mtls_with_auto_registration(port: int = 8011, proxy_url: str = "https://localhost:3004", 
                                         server_id: str = "mcp_proxy_adapter") -> Dict[str, Any]:
        """Create mTLS configuration with automatic proxy registration."""
        return (ConfigBuilder()
                .set_protocol(Protocol.MTLS)
                .set_server(port=port)
                .enable_auto_registration(proxy_url=proxy_url, server_id=server_id)
                .build())


def create_config_from_flags(protocol: str, token: bool = False, roles: bool = False, port: int = 8000, 
                           proxy_registration: bool = False, proxy_url: str = "http://localhost:3004",
                           auto_registration: bool = False, server_id: str = "mcp_proxy_adapter") -> Dict[str, Any]:
    """
    Create configuration from command line flags.
    
    Args:
        protocol: Protocol type (http, https, mtls)
        token: Enable token authentication
        roles: Enable role-based access control
        port: Server port
        proxy_registration: Enable proxy registration with manual settings
        proxy_url: Proxy URL for registration
        auto_registration: Enable automatic proxy registration (auto-determined parameters)
        server_id: Server ID for registration
        
    Returns:
        Configuration dictionary
    """
    protocol_map = {
        "http": Protocol.HTTP,
        "https": Protocol.HTTPS,
        "mtls": Protocol.MTLS
    }
    
    if protocol not in protocol_map:
        raise ValueError(f"Unsupported protocol: {protocol}")
    
    builder = ConfigBuilder().set_protocol(protocol_map[protocol]).set_server(port=port)
    
    if roles:
        builder.set_auth(AuthMethod.TOKEN_ROLES)
    elif token:
        builder.set_auth(AuthMethod.TOKEN)
    else:
        builder.set_auth(AuthMethod.NONE)
    
    # Enable proxy registration if requested
    if auto_registration:
        # Use automatic registration with auto-determined parameters
        builder.enable_auto_registration(proxy_url=proxy_url, server_id=server_id)
    elif proxy_registration:
        # Use manual registration settings
        builder.set_proxy_registration(proxy_url=proxy_url)
    
    return builder.build()


if __name__ == "__main__":
    # Example usage
    config = create_config_from_flags("http", token=True, port=8001)
    print(json.dumps(config, indent=2))
