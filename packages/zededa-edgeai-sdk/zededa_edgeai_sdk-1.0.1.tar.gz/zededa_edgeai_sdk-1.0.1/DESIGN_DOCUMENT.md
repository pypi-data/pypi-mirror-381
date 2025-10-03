# Zededa EdgeAI SDK - Dual Usage Design Document

## Overview

This document outlines the design for transforming the current `zededa-edgeai-login` package into a comprehensive `zededa-edgeai-sdk` that supports both:
1. **Command-line executable usage** with subcommands
2. **Python library usage** for programmatic integration

## Current State Analysis

### Existing Structure
- **Package Name**: `edgeai-sdk` (but entry point uses `zededa-edgeai-login`)
- **Main Module**: `edgeai_sdk.edgeai_sdk`
- **Current Functionality**: OAuth login with catalog-scoped authentication
- **Output**: Sets environment variables and spawns new shell

### API Analysis
Based on the OpenAPI spec at `https://studio.edgeai.zededa.dev/openapi.json`:

**Key Endpoints:**
- `POST /api/v1/auth/login` - Login with email/password, optional catalog scoping
- `GET /api/v1/catalogs` - List accessible catalogs  
- `GET /api/v1/user-info` - Get user information with catalog access
- `POST /api/v1/auth/logout` - Logout
- `POST /api/v1/auth/refresh` - Refresh token

**Login Endpoint Details:**
```json
{
  "operationId": "login_api_v1_auth_login_post",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {"$ref": "#/components/schemas/LoginRequest"}
      }
    }
  }
}

// LoginRequest schema
{
  "properties": {
    "email": {"type": "string"},
    "password": {"type": "string"},
    "catalog_id": {"anyOf": [{"type": "string"}, {"type": "null"}]}
  },
  "required": ["email", "password"]
}
```

## Design Requirements

### 1. Command-Line Interface Requirements
- **New executable name**: `zededa-edgeai-sdk`
- **Subcommand structure**: `zededa-edgeai-sdk <command> [options]`
- **Current command**: `login --catalog <catalog_name>`
- **Enhanced login logic**:
  - If `--catalog` provided: Use specific catalog
  - If no `--catalog`: Auto-detect single catalog access and get catalog-scoped token
  - If multiple catalogs: Require user to specify catalog

### 2. Python Library Requirements
- **Import usage**: `import zededa_edgeai_sdk` or `from zededa_edgeai_sdk import login`
- **Function**: `zededa_edgeai_sdk.login(catalog_id, email=None, password=None)`
- **Authentication modes**:
  - **Browser OAuth**: `login(catalog_id="dev")` - Opens browser for authentication
  - **Programmatic**: `login(catalog_id="dev", email="user@example.com", password="secret")`
- **Behavior**: Set environment variables (same as CLI)
- **Required parameter**: `catalog_id` must be provided (error if not)

### 3. New Backend API Requirement
**Missing API**: Catalog-scoped token endpoint
- **Purpose**: Get catalog-scoped token after general login
- **Usage**: When user has single catalog access, automatically get scoped token

## Proposed Design

### 1. Package Structure Redesign

```
zededa_edgeai_sdk/
├── __init__.py              # Main library interface
├── cli/
│   ├── __init__.py
│   ├── main.py             # CLI entry point and command router
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── login.py        # Login command implementation
│   │   ├── logout.py       # Future: Logout command
│   │   └── catalog.py      # Future: Catalog management commands
│   └── utils.py            # CLI-specific utilities
├── core/
│   ├── __init__.py
│   ├── client.py           # Main API client class
│   ├── auth.py             # Authentication logic
│   ├── oauth.py            # OAuth flow implementation (existing)
│   └── config.py           # Configuration management
├── exceptions.py           # Custom exceptions
└── utils.py                # Shared utilities
```

### 2. Entry Points Configuration

**setup.py / pyproject.toml changes:**
```toml
[project]
name = "zededa-edgeai-sdk"
# ... other config

[project.scripts]
zededa-edgeai-sdk = "zededa_edgeai_sdk.cli.main:main"

# Optional: Keep backward compatibility
zededa-edgeai-login = "zededa_edgeai_sdk.cli.main:legacy_login_main"
```

### 3. Command-Line Interface Design

#### Main CLI Structure
```bash
# Primary interface
zededa-edgeai-sdk login [--catalog <name>] [--debug]
zededa-edgeai-sdk logout [--debug]
zededa-edgeai-sdk catalog list
zededa-edgeai-sdk catalog create <name>
zededa-edgeai-sdk --version
zededa-edgeai-sdk --help
```

#### Enhanced Login Flow
```python
# Pseudocode for login command logic
def login_command(catalog_name=None):
    if catalog_name:
        # Direct catalog login (existing flow)
        return oauth_login(catalog_name)
    
    else:
        # New enhanced flow
        # 1. Do general login (without catalog scope)
        general_token = oauth_login_general()
        
        # 2. Get user's accessible catalogs
        catalogs = get_user_catalogs(general_token)
        
        if len(catalogs) == 0:
            raise NoAccessError("No catalogs accessible")
        elif len(catalogs) == 1:
            # Auto-select single catalog and get scoped token
            catalog_id = catalogs[0]['catalog_id']
            print(f"Auto-selecting catalog: {catalog_id}")
            scoped_token = get_catalog_scoped_token(general_token, catalog_id)
            return setup_environment(scoped_token, catalog_id)
        else:
            # Multiple catalogs - interactive selection
            print("Multiple catalogs available. Please select:")
            for i, cat in enumerate(catalogs, 1):
                print(f"  {i}. {cat['catalog_id']} - {cat.get('description', 'No description')}")
            
            while True:
                try:
                    choice = input(f"Enter selection (1-{len(catalogs)}): ").strip()
                    idx = int(choice) - 1
                    if 0 <= idx < len(catalogs):
                        selected_catalog = catalogs[idx]
                        catalog_id = selected_catalog['catalog_id']
                        print(f"Proceeding with catalog: {catalog_id}")
                        scoped_token = get_catalog_scoped_token(general_token, catalog_id)
                        return setup_environment(scoped_token, catalog_id)
                    else:
                        print("Invalid selection. Please try again.")
                except (ValueError, KeyboardInterrupt):
                    print("\nOperation cancelled.")
                    return None
```

### 4. Python Library Interface Design

#### Main Library Interface (`__init__.py`)
```python
"""
Zededa EdgeAI SDK

Provides both CLI and programmatic access to Zededa EdgeAI platform.
"""

from .core.client import ZededaEdgeAIClient
from .core.auth import login, logout
from .exceptions import (
    ZededaSDKError,
    AuthenticationError, 
    CatalogNotFoundError,
    MultipleCatalogsError
)

__version__ = "2.0.0"
__all__ = [
    'ZededaEdgeAIClient',
    'login',
    'logout',
    'ZededaSDKError',
    'AuthenticationError',
    'CatalogNotFoundError',
    'MultipleCatalogsError'
]
```

#### Library Usage Examples
```python
# Example 1: Browser-based OAuth (opens browser automatically)
from zededa_edgeai_sdk import login

# This will open browser for authentication and set environment variables
credentials = login(catalog_id="development")
print(f"Logged in to catalog: development")
print(f"MLflow URI: {credentials['mlflow_tracking_uri']}")

# Example 2: Programmatic authentication (no browser)
from zededa_edgeai_sdk import login

credentials = login(
    catalog_id="development",
    email="user@example.com", 
    password="secret123"
)

# Example 3: Class-based usage for more control
from zededa_edgeai_sdk import ZededaEdgeAIClient

client = ZededaEdgeAIClient()
# Browser-based login
credentials = client.login(catalog_id="development")
# OR programmatic login
credentials = client.login(catalog_id="development", email="user@example.com", password="secret")
client.logout()

# Example 4: Error handling
from zededa_edgeai_sdk import login, CatalogNotFoundError

try:
    credentials = login(catalog_id="nonexistent")
except CatalogNotFoundError:
    print("Catalog not found or no access")
```

### 5. New Backend API Specification

**Required New Endpoint:**
```yaml
# POST /api/v1/auth/catalog-scoped-token
paths:
  /api/v1/auth/catalog-scoped-token:
    post:
      tags: ["Authentication"]
      summary: "Get Catalog Scoped Token" 
      description: |
        Exchange a general access token for a catalog-scoped token.
        
        This endpoint allows users who have already authenticated with a general token
        to obtain a catalog-specific token with appropriate permissions for that catalog.
        The user must have access to the specified catalog.
        
        Use cases:
        - CLI auto-selection of single accessible catalog
        - Switching between catalogs without re-authentication
        - Obtaining minimal-privilege tokens for specific operations
        
      security:
        - HTTPBearer: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CatalogScopedTokenRequest'
      responses:
        200:
          description: "Successful Response"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CatalogScopedTokenResponse'
        403:
          description: "No access to specified catalog"
        422:
          description: "Validation Error"

components:
  schemas:
    CatalogScopedTokenRequest:
      type: object
      required: ["catalog_id"]
      properties:
        catalog_id:
          type: string
          description: "ID of the catalog to scope the token to"
          example: "development"
    
    CatalogScopedTokenResponse:
      type: object
      required: ["access_token", "catalog_id", "user_permissions"]
      properties:
        access_token:
          type: string
          description: "Catalog-scoped JWT token"
        token_type:
          type: string
          default: "bearer"
        expires_in:
          type: integer
          default: 3600
          description: "Token expiration time in seconds"
        catalog_id:
          type: string
          description: "Catalog ID this token is scoped to"
        user_permissions:
          type: array
          items:
            type: string
          description: "User's permissions in this catalog"
          example: ["read", "write", "deploy"]
        catalog_info:
          $ref: '#/components/schemas/CatalogInfo'
          description: "Information about the catalog"
```

### 6. Core Components Design

#### Authentication Flow Manager (`core/auth.py`)
```python
class AuthenticationManager:
    """Handles all authentication flows"""
    
    def __init__(self, service_url: str):
        self.service_url = service_url
        
    def oauth_login(self, catalog_id: str = None) -> dict:
        """OAuth login with optional catalog scoping"""
        
    def get_catalog_scoped_token(self, general_token: str, catalog_id: str) -> dict:
        """Get catalog-scoped token using new API"""
        
    def get_user_catalogs(self, token: str) -> list:
        """Get list of accessible catalogs"""
        
    def refresh_token(self, refresh_token: str) -> dict:
        """Refresh access token"""
```

#### Main Client Class (`core/client.py`)
```python
class ZededaEdgeAIClient:
    """Main client class for Zededa EdgeAI SDK"""
    
    def __init__(self, backend_url: str = None, debug: bool = False):
        self.backend_url = backend_url or DEFAULT_BACKEND_URL
        self.auth_manager = AuthenticationManager(self.backend_url)
        self.debug = debug
        
    def login(self, catalog_id: str, email: str = None, password: str = None) -> dict:
        """
        Login to specific catalog and set environment variables
        
        Args:
            catalog_id: Required catalog ID to login to
            email: Email for programmatic auth (optional, triggers browser OAuth if not provided)
            password: Password for programmatic auth (required if email provided)
            
        Returns:
            dict: Credentials dictionary with tokens and endpoints
            
        Raises:
            CatalogNotFoundError: If catalog doesn't exist or no access
            AuthenticationError: If authentication fails
            ValueError: If email provided but password missing
        """
        
    def logout(self) -> bool:
        """Logout and clear environment variables"""
        
    def list_catalogs(self) -> list:
        """List accessible catalogs"""
        
    def get_current_catalog(self) -> str:
        """Get currently active catalog from environment"""
```

### 7. Environment Variable Management

**Enhanced Environment Setup:**
```python
def setup_environment(credentials: dict, catalog_id: str) -> dict:
    """Set up environment variables for MLflow and MinIO access"""
    
    env_vars = {
        "ZEDEDA_CURRENT_CATALOG": catalog_id,
        "ZEDEDA_ACCESS_TOKEN": credentials["backend_jwt"],
        "MLFLOW_TRACKING_TOKEN": credentials["backend_jwt"],
        "MLFLOW_TRACKING_URI": credentials["mlflow_tracking_uri"],
        "AWS_ACCESS_KEY_ID": credentials["aws_access_key_id"],
        "AWS_SECRET_ACCESS_KEY": credentials["aws_secret_access_key"],
        "MLFLOW_S3_ENDPOINT_URL": credentials["endpoint_url"],
        "MINIO_BUCKET": credentials["bucket"],
        # New variables for better SDK integration
        "ZEDEDA_BACKEND_URL": credentials.get("backend_url"),
        "ZEDEDA_CATALOG_PERMISSIONS": ",".join(credentials.get("permissions", []))
    }
    
    # Set in current process
    for key, value in env_vars.items():
        if value:
            os.environ[key] = str(value)
    
    return env_vars
```



## Implementation Examples

### Command-Line Usage Examples

```bash
# Basic login with interactive selection
zededa-edgeai-sdk login
# -> Auto-detects single catalog or shows interactive menu:
# Multiple catalogs available. Please select:
#   1. development - Development environment
#   2. staging - Staging environment
#   3. production - Production environment
# Enter selection (1-3): 2

# Specific catalog login
zededa-edgeai-sdk login --catalog development

# Future commands
zededa-edgeai-sdk logout
zededa-edgeai-sdk catalog list
zededa-edgeai-sdk catalog create production --description "Production environment"
```

### Python Library Usage Examples

```python
# Example 1: Browser-based authentication (opens browser)
import os
from zededa_edgeai_sdk import login

# Login via browser and set environment variables
credentials = login(catalog_id="development")  # Opens browser

# Now MLflow SDK can be used directly
import mlflow
mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
# MLflow will use the auth token from environment automatically

# Example 2: Programmatic authentication (no browser needed)
from zededa_edgeai_sdk import login

# Direct authentication for automation/scripts
credentials = login(
    catalog_id="development",
    email="user@example.com",
    password="secret123"
)

# Example 3: Context manager usage
from zededa_edgeai_sdk import ZededaEdgeAIClient

with ZededaEdgeAIClient() as client:
    # Browser-based auth
    creds = client.login("development")
    # OR programmatic auth
    # creds = client.login("development", email="user@example.com", password="secret")
    
    # Use MLflow within this context
    import mlflow
    with mlflow.start_run():
        mlflow.log_param("model_type", "classification")
        # ... training code
    
# Environment automatically cleaned up

# Example 4: Multiple catalog workflow
client = ZededaEdgeAIClient()

# Login to development catalog
dev_creds = client.login("development")
# ... do development work

# Switch to staging catalog  
staging_creds = client.login("staging")
# ... do staging work

client.logout()

# Example 5: Error handling
from zededa_edgeai_sdk import login, CatalogNotFoundError, AuthenticationError

try:
    credentials = login(catalog_id="my-catalog")
except CatalogNotFoundError:
    print("Catalog 'my-catalog' not found or you don't have access")
except AuthenticationError as e:
    print(f"Authentication failed: {e}")
    
# Example 6: Integration with automation scripts
def setup_ml_environment(catalog: str, email: str, password: str):
    """Setup ML environment for specific catalog - automation friendly"""
    from zededa_edgeai_sdk import login
    
    try:
        # Programmatic login - no browser interaction
        creds = login(catalog_id=catalog, email=email, password=password)
        print(f"Environment ready for catalog: {catalog}")
        return creds
    except Exception as e:
        print(f"Failed to setup environment: {e}")
        return None

if __name__ == "__main__":
    # For automation - reads from environment or config
    email = os.getenv("ZEDEDA_EMAIL")
    password = os.getenv("ZEDEDA_PASSWORD")
    setup_ml_environment("production", email, password)
    
    # Now run your ML code
    import mlflow
    # MLflow will automatically use the configured environment
```

## Benefits of This Design

### 1. **Unified Experience**
- Single package supports both CLI and library usage
- Consistent authentication flow across both interfaces
- Shared configuration and error handling

### 2. **Enhanced Usability**
- CLI auto-detection of single catalog access with interactive selection for multiple catalogs
- Clear subcommand structure for future extensibility
- Dual authentication modes: browser OAuth for interactive use, programmatic for automation
- Programmatic access for automation and integration

### 3. **Flexible Authentication**
- **Browser OAuth**: Perfect for interactive development and exploration
- **Programmatic Auth**: Ideal for CI/CD, automation scripts, and headless environments
- **Same Environment Setup**: Both modes result in identical environment variable configuration

### 4. **Future Extensibility**
- Clear structure for adding new commands (catalog management, etc.)
- Modular design allows easy addition of new features
- Plugin architecture possible for advanced users

### 5. **Better Error Handling**
- Specific exceptions for different error conditions
- Clear error messages and suggestions
- Graceful handling of edge cases
- Interactive prompts with validation

## Next Steps

1. **Backend API Implementation**: Implement the new catalog-scoped token endpoint
2. **Package Restructuring**: Reorganize code according to new structure
3. **CLI Framework**: Implement subcommand-based CLI with interactive selection using `click` or `argparse`
4. **Library Interface**: Create clean Python library interface with dual authentication modes
5. **Testing**: Comprehensive testing of both CLI and library interfaces
6. **Documentation**: Update documentation with new usage patterns

This design provides a solid foundation for a dual-purpose SDK that can grow with your platform's needs while maintaining compatibility and usability.