# ebraconys

Utility functions for common Python tasks by Ebraconys Labs.

## Installation

```bash
pip install ebraconys
```

## Usage

```python
from ebraconys import string_utils, math_utils

# String utilities
result = string_utils.slugify("Hello World!")
print(result)  # "hello-world"

# Math utilities
total = math_utils.percentage(25, 100)
print(total)  # 25.0
```

## License

MIT


# Development

### 1. **Build and Deploy to PyPI**

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Upload to PyPI (using organization credentials)
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

### 2. **Authentication with Organization**

When prompted for credentials:
- **Username**: `__token__`
- **Password**: Your organization API token (from PyPI → Account Settings → API tokens)

Create a token with:
- **Scope**: Entire account (or just the ebraconys-labs organization)
- **Permissions**: All (for first deployment)

### 3. **Verify Installation**

```bash
# Test the installation
pip install ebraconys

# Test in Python
python -c "from ebraconys import slugify; print(slugify('Hello from Ebraconys Labs!'))"
```

## 🎯 What You'll Get:

- **Package URL**: `https://pypi.org/project/ebraconys-labs-utils/`
- **Organization**: Managed under `ebraconys-labs`
- **Installable via**: `pip install ebraconys-labs-utils`

## 🔧 Next Steps:

1. **Create GitHub repository** for the project
2. **Set up CI/CD** for automatic deployments
3. **Add more utility functions** as needed
4. **Invite collaborators** to your organization

Your package will now be live on PyPI under the ebraconys-labs organization! 🎉

