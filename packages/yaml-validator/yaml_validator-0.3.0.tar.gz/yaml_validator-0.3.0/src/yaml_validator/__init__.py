"""YAML Validator - Validate user YAML configuration files against templates."""

from .validator import validate_config, extract_annotations, validate_config_recursive

__version__ = "0.1.0"
__all__ = ["validate_config", "extract_annotations", "validate_config_recursive"]
