# devkit

Command-line utilities for everyday development tasks.

## Features

- **json-format**: Pretty-print and validate JSON files
- **env-check**: Validate environment variables against schema
- **More utilities**: Additional tools for common workflows

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Format JSON
devkit json-format input.json

# Format with custom indentation
devkit json-format input.json --indent 4

# Check environment
devkit env-check --schema .env.schema
```

## Examples

```bash
# Pretty-print a minified JSON file
devkit json-format package.json

# Validate environment variables before deployment
devkit env-check --schema production.schema
```

## Requirements

- Python 3.8+

## License

MIT
