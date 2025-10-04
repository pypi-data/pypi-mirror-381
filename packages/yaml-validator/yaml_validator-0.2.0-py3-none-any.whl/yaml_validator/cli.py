"""Command-line interface for YAML validator."""

import sys
from .validator import validate_config


def main():
    """Main entry point for the CLI."""
    if len(sys.argv) != 3:
        print("Usage: yaml-validator <user_config.yaml> <default_config.yaml>")
        sys.exit(1)

    user_file = sys.argv[1]
    default_file = sys.argv[2]

    try:
        if not validate_config(user_file, default_file):
            sys.exit(1)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error validating configuration: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
