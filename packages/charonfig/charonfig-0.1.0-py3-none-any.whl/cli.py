# src/charonfig/cli.py
import argparse
import importlib.util
import os
import sys
from typing import Type
from charonfig import BaseConfig, CharonfigError, MissingRequiredFieldError, TypeValidationError, EncryptionError
from cryptography.fernet import Fernet 


def load_schema_module(schema_path: str) -> Type[BaseConfig]:
    """Dynamically load the schema class from the given file path."""
    if not os.path.exists(schema_path):
        raise CharonfigError(f"Schema file not found: {schema_path}")
    
    module_name = os.path.splitext(os.path.basename(schema_path))[0]
    
    spec = importlib.util.spec_from_file_location(module_name, schema_path)
    if spec is None or spec.loader is None:
            raise CharonfigError(f"Could not load module from {schema_path}")
    
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    
    # Find the class that inherits from BaseConfig
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if isinstance(attr, type) and issubclass(attr, BaseConfig) and attr is not BaseConfig:
            return attr
    
    raise CharonfigError(f"No subclass of BaseConfig found in the provided schema file '{schema_path}'.")

def generate_config(args: argparse.Namespace) -> None:
    """Generate a config file from the schema."""
    try:
        schema_class = load_schema_module(args.schema)
        encryption_key = Fernet.generate_key() if args.encrypt and not args.encryption_key else args.encryption_key
        config = schema_class(
            env_prefix=args.env_prefix,
            load_env=args.load_env,
            encryption_key=encryption_key
        )
        config.to_file(args.output, format=args.format, include_comments=True)
        if args.encrypt and encryption_key:
            print(f"Generated encryption key: {encryption_key.decode()}")
    except CharonfigError as e:
        print(f"Error: {e}")
        sys.exit(1)

def validate_config(args: argparse.Namespace) -> None:
    """Validate configuration against the schema."""
    try:
        schema_class = load_schema_module(args.schema)
        config = schema_class(
            env_prefix=args.env_prefix,
            load_env=args.load_env,
            encryption_key=args.encryption_key
        )
        config.validate_all()
        print("Validation successful!")
        print("Configuration:", config.to_dict(decrypt=True))
    except MissingRequiredFieldError as e:
        print(f"Missing required field: {e}")
        sys.exit(1)
    except TypeValidationError as e:
        print(f"Type validation error: {e}")
        sys.exit(1)
    except EncryptionError as e:
        print(f"Encryption error: {e}")
        sys.exit(1)
    except CharonfigError as e:
        print(f"Error: {e}")
        sys.exit(1)

def show_schema(args: argparse.Namespace) -> None:
    """Display the schema's fields and metadata."""
    try:
        schema_class = load_schema_module(args.schema)
        print(f"Schema: {schema_class.__name__}")
        print("Fields:")
        for name, field in schema_class._fields.items():
            print(f"  {name}:")
            print(f"    Type: {field.__class__.__name__}")
            print(f"    Required: {field.required}")
            if field.default is not None:
                print(f"    Default: {repr(field.default)}")
            else:
                print(f"    Default: None")
            print(f"    Sensitive: {field.sensitive}")
            print(f"    Description: {field.description or 'None'}")
    except CharonfigError as e:
        print(f"Error: {e}")
        sys.exit(1)

def generate_docs(args: argparse.Namespace) -> None:
    """Generate documentation for the schema."""
    try:
        schema_class = load_schema_module(args.schema)
        instance = schema_class(skip_initial_validation=True)
        instance.generate_docs(args.output)
    except CharonfigError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Charonfig CLI: Schema-first configuration management",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True, help="Command to execute")

    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate a config file from a schema")
    generate_parser.add_argument("schema", help="Path to the schema Python file (e.g., schema.py)")
    generate_parser.add_argument("--format", choices=["env", "json", "yaml"], default="env", help="Output file format")
    generate_parser.add_argument("--output", default="config.env", help="Output file path")
    generate_parser.add_argument("--env-prefix", default=None, help="Prefix for environment variables")
    generate_parser.add_argument("--no-load-env", action="store_false", dest="load_env", help="Disable loading from environment variables")
    generate_parser.add_argument("--encrypt", action="store_true", help="Enable encryption for sensitive fields (generates key if not provided)")
    generate_parser.add_argument("--encryption-key", type=lambda x: x.encode() if isinstance(x, str) else x, default=None, help="Fernet encryption key (base64-encoded string)")

    # Validate command
    validate_parser = subparsers.add_parser("validate", help="Validate configuration against the schema")
    validate_parser.add_argument("schema", help="Path to the schema Python file (e.g., schema.py)")
    validate_parser.add_argument("--env-prefix", default=None, help="Prefix for environment variables")
    validate_parser.add_argument("--no-load-env", action="store_false", dest="load_env", help="Disable loading from environment variables")
    validate_parser.add_argument("--encryption-key", type=lambda x: x.encode() if isinstance(x, str) else x, default=None, help="Fernet encryption key (base64-encoded string)")

    # Show command
    show_parser = subparsers.add_parser("show", help="Display the schema's fields and metadata")
    show_parser.add_argument("schema", help="Path to the schema Python file (e.g., schema.py)")

    # Docs command
    docs_parser = subparsers.add_parser("docs", help="Generate Markdown documentation from the schema")
    docs_parser.add_argument("schema", help="Path to the schema Python file (e.g., schema.py)")
    docs_parser.add_argument("--output", default="config_docs.md", help="Output Markdown file path")

    args = parser.parse_args()

    if args.command == "generate":
        generate_config(args)
    elif args.command == "validate":
        validate_config(args)
    elif args.command == "show":
        show_schema(args)
    elif args.command == "docs":
        generate_docs(args)

if __name__ == "__main__":
    main()