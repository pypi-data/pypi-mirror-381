# YAML Validator

A Python utility for validating user YAML configuration files against a default/template YAML file with support for optional fields.

## Features

- Validates that required keys from a default YAML are present in a user YAML
- Supports marking keys as optional using `#optional` comments
- Type checking between user and default configurations
- Recursive validation for nested YAML structures
- Clear error messages indicating missing keys or type mismatches

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

### Command Line

```bash
./yaml_validator.py <user_config.yaml> <default_config.yaml>
```

#### Arguments

- `user_config.yaml`: The YAML file to validate
- `default_config.yaml`: The template/default YAML file with annotations

#### Exit Codes

- `0`: Validation successful
- `1`: Validation failed (missing required keys or type mismatches)

### Importing in Python Projects

```python
from yaml_validator import validate_config

# Validate a user config against a default template
is_valid = validate_config('user_config.yaml', 'default_config.yaml')

if is_valid:
    print("Configuration is valid!")
else:
    print("Configuration validation failed.")
    # Handle the error appropriately
```

The `validate_config` function returns `True` if validation passes, `False` otherwise. Validation errors are printed to stdout.

## Annotation Syntax

In your default YAML file, mark optional keys with `#optional`:

```yaml
database:
  host: localhost
  port: 5432
  username: admin
  password: secret  #optional
  ssl_enabled: true  #optional
```

Keys without `#optional` are treated as required.

## Validation Rules

1. **Required Keys**: Keys in the default file without `#optional` must exist in the user file
2. **Type Matching**: When a key exists in both files, the value types must match
3. **Nested Validation**: Nested dictionaries are validated recursively
4. **Optional Keys**: Keys marked with `#optional` can be omitted from the user file

## Example

**default.yaml:**
```yaml
app:
  name: MyApp
  version: 1.0
  debug: false  #optional
  database:
    host: localhost
    port: 5432
```

**user.yaml:**
```yaml
app:
  name: MyApp
  version: 1.0
  database:
    host: db.example.com
    port: 5432
```

Running the validator:
```bash
./yaml_validator.py user.yaml default.yaml
# Exit code 0 - validation passes
```

## How It Works

1. **Annotation Extraction** (`extract_annotations`): Parses the default YAML file to identify which keys are optional or required based on `#optional` comments
2. **Recursive Validation** (`validate_config_recursive`): Traverses both YAML structures simultaneously, checking for missing keys and type mismatches
3. **Error Reporting**: Prints detailed messages for each validation failure with the full key path
