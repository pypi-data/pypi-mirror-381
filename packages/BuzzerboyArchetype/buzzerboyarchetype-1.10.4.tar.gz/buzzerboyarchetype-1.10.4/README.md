# Buzzerboy Archetype

A standardized architecture framework for Buzzerboy-based applications that provides consistent project naming, configuration, and deployment patterns across different environments and tiers.

## Overview

The Buzzerboy Archetype is a Python package that standardizes how Buzzerboy applications are structured, named, and configured. It provides a consistent interface for defining project metadata including product names, application names, deployment tiers, and AWS infrastructure settings.

## Features

- **Standardized Project Naming**: Consistent naming convention across all Buzzerboy projects
- **Multi-Tier Support**: Support for different deployment environments (dev, staging, production)
- **AWS Integration**: Built-in support for AWS regions and resource naming
- **Secret Management**: Standardized secret naming and organization
- **Domain Management**: Automatic domain name generation based on project structure

## Installation

Install the package using pip:

```bash
pip install BuzzerboyArchetype
```

## Quick Start

```python
from BuzzerboyArchetypeStack import BuzzerboyArchetype

# Create an archetype instance
archetype = BuzzerboyArchetype(
    product='myproduct',
    app='myapp',
    tier='dev',
    organization='buzzerboy',
    region='ca-central-1'  # Optional, defaults to ca-central-1
)

# Get standardized project information
project_name = archetype.get_project_name()  # Returns: myproduct-myapp-dev
domain_name = archetype.get_domain_name()    # Returns: myproduct-myapp-dev.buzzerboy.com
secret_name = archetype.get_secret_name()    # Returns: buzzerboy/dev/myproduct-myapp-dev
```

## API Reference

### BuzzerboyArchetype Class

#### Constructor

```python
BuzzerboyArchetype(product, app, tier, organization, region='ca-central-1')
```

**Parameters:**
- `product` (str): The product name
- `app` (str): The application name
- `tier` (str): The deployment tier (e.g., 'dev', 'staging', 'prd')
- `organization` (str): The organization name
- `region` (str, optional): AWS region, defaults to 'ca-central-1'

#### Methods

- `get_project_name()`: Returns the standardized project name in format `{product}-{app}-{tier}`
- `get_tier()`: Returns the deployment tier, defaults to 'dev' if not specified
- `get_domain_name()`: Returns the domain name in format `{project_name}.{organization}.com`
- `get_secret_name()`: Returns the secret path in format `{organization}/{tier}/{project_name}`
- `get_region()`: Returns the AWS region
- `set_stack(stack)`: Associates a stack object with the archetype

## Usage Examples

### Basic Usage

```python
from BuzzerboyArchetypeStack import BuzzerboyArchetype

# Development environment
dev_archetype = BuzzerboyArchetype(
    product='productname',
    app='appname',
    tier='tier',
    organization='client'
)

print(f"Project: {dev_archetype.get_project_name()}")
print(f"Domain: {dev_archetype.get_domain_name()}")
print(f"Secrets: {dev_archetype.get_secret_name()}")
```

### Multi-Environment Setup

```python
from BuzzerboyArchetypeStack import BuzzerboyArchetype

environments = ['dev', 'staging', 'prd']
archetypes = {}

for env in environments:
    archetypes[env] = BuzzerboyArchetype(
        product='myproduct',
        app='myapp',
        tier=env,
        organization='buzzerboy'
    )
    
    print(f"{env}: {archetypes[env].get_project_name()}")
```

## Integration with Infrastructure

This archetype is commonly used with infrastructure-as-code tools. For example, with AWS CDK or Terraform:

```python
from BuzzerboyArchetypeStack import BuzzerboyArchetype
# Example integration (actual implementation may vary)

archetype = BuzzerboyArchetype(
    product='productname',
    app='appname',
    tier='tiername',
    organization='clientname'
)

# Use archetype values for infrastructure
infrastructure_config = {
    'project_name': archetype.get_project_name(),
    'environment': archetype.get_tier(),
    'domain_name': archetype.get_domain_name(),
    'region': archetype.get_region(),
    'secret_name': archetype.get_secret_name()
}
```

## Development

### Prerequisites

- Python >= 3.8
- setuptools >= 61.0

### Building

The project uses `pyproject.toml` for configuration and setuptools for building:

```bash
pip install build
python -m build
```

### Version Management

The project uses semantic versioning. 

## Contributing

This project is internally managed by Buzzerboy Inc

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
- **Homepage**: https://www-dev.buzzerboy.com/
