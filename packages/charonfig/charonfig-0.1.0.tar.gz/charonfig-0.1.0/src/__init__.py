# src/charonfig/__init__.py
import os
import json
import yaml
from typing import Any, Dict, Optional, Union, Type, Protocol
from cryptography.fernet import Fernet, InvalidToken

# Custom exceptions for specific error types
class CharonfigError(Exception):
    """Base exception for Charonfig errors."""
    pass

class MissingRequiredFieldError(CharonfigError):
    """Raised when a required field is missing."""
    pass

class TypeValidationError(CharonfigError):
    """Raised when a field value has an incorrect type."""
    pass

class EncryptionError(CharonfigError):
    """Raised when encryption or decryption fails."""
    pass

class Field(Protocol):
    """Protocol for configuration fields."""
    required: bool
    default: Any
    description: str
    sensitive: bool
    name: Optional[str]
    def validate(self, value: Any) -> Any: ...
    def encrypt(self, value: Any, fernet: Optional[Fernet]) -> str: ...
    def decrypt(self, encrypted_value: str, fernet: Optional[Fernet]) -> Any: ...

class StringField:
    """A field for string values."""
    def __init__(self, required: bool = False, default: Any = None, description: str = "", sensitive: bool = False):
        self.required = required
        self.default = default
        self.description = description
        self.sensitive = sensitive
        self.name = None

    def validate(self, value: Any) -> Optional[str]:
        if value is None and self.required and self.default is None:
            raise MissingRequiredFieldError(f"Field '{self.name or 'unknown'}' is required and has no default.")
        if value is not None and not isinstance(value, str):
            raise TypeValidationError(f"Expected a string, but got {type(value).__name__}.")
        return value

    def encrypt(self, value: Any, fernet: Optional[Fernet]) -> str:
        if not self.sensitive or value is None or fernet is None:
            return str(value) if value is not None else ""
        try:
            return fernet.encrypt(str(value).encode()).decode()
        except Exception as e:
            raise EncryptionError(f"Failed to encrypt value for field '{self.name or 'unknown'}': {e}")

    def decrypt(self, encrypted_value: str, fernet: Optional[Fernet]) -> Any:
        if not self.sensitive or not encrypted_value or fernet is None:
            return encrypted_value
        try:
            return fernet.decrypt(encrypted_value.encode()).decode()
        except InvalidToken as e:
            raise EncryptionError(f"Failed to decrypt value for field '{self.name or 'unknown'}': {e}")

class IntegerField:
    """A field for integer values."""
    def __init__(self, required: bool = False, default: Any = None, description: str = "", sensitive: bool = False):
        self.required = required
        self.default = default
        self.description = description
        self.sensitive = sensitive
        self.name = None

    def validate(self, value: Any) -> Optional[int]:
        if value is None and self.required and self.default is None:
            raise MissingRequiredFieldError(f"Field '{self.name or 'unknown'}' is required and has no default.")
        if value is not None:
            try:
                return int(value)
            except (ValueError, TypeError):
                raise TypeValidationError(f"Expected an integer, but got '{value}'.")
        return value

    def encrypt(self, value: Any, fernet: Optional[Fernet]) -> str:
        if not self.sensitive or value is None or fernet is None:
            return str(value) if value is not None else ""
        try:
            return fernet.encrypt(str(value).encode()).decode()
        except Exception as e:
            raise EncryptionError(f"Failed to encrypt value for field '{self.name or 'unknown'}': {e}")

    def decrypt(self, encrypted_value: str, fernet: Optional[Fernet]) -> Any:
        if not self.sensitive or not encrypted_value or fernet is None:
            return encrypted_value
        try:
            return int(fernet.decrypt(encrypted_value.encode()).decode())
        except (InvalidToken, ValueError) as e:
            raise EncryptionError(f"Failed to decrypt value for field '{self.name or 'unknown'}': {e}")

class BooleanField:
    """A field for boolean values."""
    def __init__(self, required: bool = False, default: Any = None, description: str = "", sensitive: bool = False):
        self.required = required
        self.default = default
        self.description = description
        self.sensitive = sensitive
        self.name = None

    def validate(self, value: Any) -> Optional[bool]:
        if value is None and self.required and self.default is None:
            raise MissingRequiredFieldError(f"Field '{self.name or 'unknown'}' is required and has no default.")
        if value is not None:
            if isinstance(value, bool):
                return value
            lower = str(value).lower()
            if lower in ['true', '1', 'yes', 'y']:
                return True
            if lower in ['false', '0', 'no', 'n']:
                return False
            raise TypeValidationError(f"Cannot interpret '{value}' as a boolean.")
        return value

    def encrypt(self, value: Any, fernet: Optional[Fernet]) -> str:
        if not self.sensitive or value is None or fernet is None:
            return str(value).lower() if value is not None else ""
        try:
            return fernet.encrypt(str(value).lower().encode()).decode()
        except Exception as e:
            raise EncryptionError(f"Failed to encrypt value for field '{self.name or 'unknown'}': {e}")

    def decrypt(self, encrypted_value: str, fernet: Optional[Fernet]) -> Any:
        if not self.sensitive or not encrypted_value or fernet is None:
            return encrypted_value
        try:
            decrypted = fernet.decrypt(encrypted_value.encode()).decode().lower()
            return decrypted in ['true', '1', 'yes', 'y']
        except InvalidToken as e:
            raise EncryptionError(f"Failed to decrypt value for field '{self.name or 'unknown'}': {e}")

class NestedField:
    """A field for nested configurations."""
    def __init__(self, config_class: Type['BaseConfig'], required: bool = False, default: Optional[Union[Type['BaseConfig'], 'BaseConfig']] = None, description: str = "", sensitive: bool = False):
        self.required = required
        self.default = default or config_class
        self.description = description
        self.sensitive = sensitive
        self.name = None
        self.config_class = config_class

    def validate(self, value: Any) -> Optional['BaseConfig']:
        if value is None and self.required and self.default is None:
            raise MissingRequiredFieldError(f"Field '{self.name or 'unknown'}' is required and has no default.")
        if value is None:
            return None
        if not isinstance(value, BaseConfig):
            raise TypeValidationError(f"Expected a BaseConfig instance for '{self.name}', but got {type(value).__name__}.")
        value.validate_all()
        return value

    def instantiate_default(self, outer_prefix: Optional[str] = None, load_env: bool = False, encryption_key: Optional[bytes] = None, skip_initial_validation: bool = True) -> 'BaseConfig':
        """Instantiate the default nested config, supporting pre-instantiated defaults."""
        if isinstance(self.default, BaseConfig):
            return self.default
        sub_prefix = f"{outer_prefix}_{self.name}" if outer_prefix and self.name else self.name or ""
        return self.config_class(env_prefix=sub_prefix, load_env=load_env, encryption_key=encryption_key, skip_initial_validation=skip_initial_validation)

    def encrypt(self, value: Any, fernet: Optional[Fernet]) -> str:
        # Nested fields don't encrypt the whole object; handled recursively
        return str(value) if value is not None else ""

    def decrypt(self, encrypted_value: str, fernet: Optional[Fernet]) -> Any:
        # Nested fields don't decrypt the whole object; handled recursively
        return encrypted_value

class BaseConfigMeta(type):
    """Metaclass to cache fields for performance and explicit registration."""
    @property
    def _fields(cls):
        if not hasattr(cls, '_cached_fields'):
            cls._cached_fields = {k: v for k, v in cls.__dict__.items() if isinstance(v, (StringField, IntegerField, BooleanField, NestedField))}
            for k in cls._cached_fields:
                cls._cached_fields[k].name = k
        return cls._cached_fields

class BaseConfig(metaclass=BaseConfigMeta):
    """Base class for a configuration schema."""
    def __init__(self, env_prefix: Optional[str] = None, load_env: bool = True, encryption_key: Optional[bytes] = None, skip_initial_validation: bool = False, **kwargs: Any):
        self._fields = self.__class__._fields.copy()  # Instance copy for mutability if needed
        self._env_prefix: Optional[str] = env_prefix.upper() if env_prefix else None
        self._fernet: Optional[Fernet] = Fernet(encryption_key or Fernet.generate_key()) if any(f.sensitive for f in self._fields.values() if hasattr(f, 'sensitive')) else None

        # Initialize with defaults using cached fields
        for name, field in self._fields.items():
            if isinstance(field, NestedField):
                default_value = field.instantiate_default(self._env_prefix, load_env=False, encryption_key=encryption_key)
            else:
                default_value = field.default
            setattr(self, name, default_value)

        # Load from environment variables if enabled
        if load_env:
            self._load_from_env()

        # Override with any provided kwargs
        for name, value in kwargs.items():
            if name in self._fields:
                field = self._fields[name]
                if isinstance(field, NestedField):
                    if isinstance(value, dict):
                        sub_prefix = f"{self._env_prefix}_{name}" if self._env_prefix else name
                        sub_config = field.config_class(env_prefix=sub_prefix, load_env=False, encryption_key=encryption_key, skip_initial_validation=False, **value)
                    else:
                        sub_config = value
                    setattr(self, name, sub_config)
                else:
                    setattr(self, name, value)
            else:
                print(f"Warning: '{name}' is not a defined field in the schema.")

        # Final validation
        if not skip_initial_validation:
            self.validate_all()

    def _load_from_env(self) -> None:
        """Load configuration values from environment variables, with decrypt support for nested."""
        for name, field in self._fields.items():
            env_name = f"{self._env_prefix}_{name}" if self._env_prefix else name
            if isinstance(field, NestedField):
                sub_prefix = f"{self._env_prefix}_{name}" if self._env_prefix else name
                sub_config = field.config_class(env_prefix=sub_prefix, load_env=True, encryption_key=self._fernet.key if self._fernet else None, skip_initial_validation=False)
                setattr(self, name, sub_config)
            else:
                if env_name in os.environ:
                    try:
                        value = os.environ[env_name]
                        if field.sensitive and self._fernet:
                            value = field.decrypt(value, self._fernet)
                        validated_value = field.validate(value)
                        setattr(self, name, validated_value)
                    except CharonfigError as e:
                        raise CharonfigError(f"Invalid environment variable {env_name}: {e}")

    def validate_all(self) -> None:
        """Validate all fields in the schema, recursively for nested."""
        for name, field in self._fields.items():
            value = getattr(self, name, None)
            if isinstance(field, NestedField):
                if value is not None:
                    value.validate_all()
                elif field.required:
                    raise MissingRequiredFieldError(f"Nested field '{name}' is required.")
            else:
                validated_value = field.validate(value)
                setattr(self, name, validated_value)
        print("Configuration validated successfully!")

    def to_dict(self, decrypt: bool = True) -> Dict[str, Any]:
        """Converts the config object to a dictionary, optionally decrypting sensitive fields."""
        result = {}
        for name, field in self._fields.items():
            value = getattr(self, name)
            if value is None:
                result[name] = None
                continue
            if isinstance(field, NestedField):
                result[name] = value.to_dict(decrypt=decrypt)
            else:
                out_value = value
                if decrypt and field.sensitive and self._fernet:
                    try:
                        out_value = field.decrypt(str(value), self._fernet)
                    except EncryptionError as e:
                        raise EncryptionError(f"Failed to decrypt field '{name}': {e}")
                result[name] = out_value
        return result

    def _generate_env_lines(self, lines: list, prefix: str = "") -> None:
        """Helper to generate flattened .env lines, encrypting sensitive fields."""
        for name, field in self._fields.items():
            full_key = f"{prefix}{name}" if prefix else name
            value = getattr(self, name)
            if value is None:
                if field.required:
                    raise MissingRequiredFieldError(f"Cannot generate .env: Required field '{full_key}' is None.")
                continue
            if isinstance(field, NestedField):
                value._generate_env_lines(lines, full_key + "_")
            else:
                value_str = field.encrypt(value, self._fernet) if self._fernet and field.sensitive else str(value)
                if isinstance(value_str, str) and any(c in value_str for c in " =#"):
                    value_str = f'"{value_str}"'
                lines.append(f"{full_key.upper()}={value_str}")

    def to_env_file(self, output_path: str = "config.env", include_comments: bool = True) -> None:
        """Generate a .env file from the configuration, flattening nested fields and encrypting sensitive fields."""
        lines = []
        if include_comments:
            self._generate_env_lines_with_comments(lines)
        else:
            self._generate_env_lines(lines, "")
        with open(output_path, "w") as f:
            f.write("\n".join(lines) + "\n")
        print(f".env file generated at: {output_path}")

    def _generate_env_lines_with_comments(self, lines: list) -> None:
        """Helper for .env with comments from descriptions."""
        for name, field in self._fields.items():
            if field.description:
                lines.append(f"# {field.description.strip()}")
            full_key = name.upper()
            value = getattr(self, name)
            if value is None:
                if field.required:
                    raise MissingRequiredFieldError(f"Cannot generate .env: Required field '{full_key}' is None.")
                continue
            if isinstance(field, NestedField):
                lines.append(f"# {field.description.strip()}" if field.description else "")
                sub_prefix = full_key + "_"
                value._generate_env_lines_with_comments_sub(lines, sub_prefix)
            else:
                value_str = field.encrypt(value, self._fernet) if self._fernet and field.sensitive else str(value)
                if isinstance(value_str, str) and any(c in value_str for c in " =#"):
                    value_str = f'"{value_str}"'
                lines.append(f"{full_key}={value_str}")

    def _generate_env_lines_with_comments_sub(self, lines: list, prefix: str) -> None:
        """Sub-helper for nested .env comments."""
        for name, field in self._fields.items():
            full_key = f"{prefix}{name.upper()}"
            if field.description:
                lines.append(f"# {field.description.strip()}")
            value = getattr(self, name)
            if value is None:
                continue
            if isinstance(field, NestedField):
                sub_prefix = full_key + "_"
                value._generate_env_lines_with_comments_sub(lines, sub_prefix)
            else:
                value_str = field.encrypt(value, self._fernet) if self._fernet and field.sensitive else str(value)
                if isinstance(value_str, str) and any(c in value_str for c in " =#"):
                    value_str = f'"{value_str}"'
                lines.append(f"{full_key}={value_str}")

    def to_file(self, output_path: str, format: str = "env", include_comments: bool = False) -> None:
        """Generate a config file in the specified format, with optional comments."""
        if format == "env":
            self.to_env_file(output_path, include_comments)
            return
        config_dict = self.to_dict(decrypt=False)
        if include_comments:
            # For YAML, we can add comments manually or use a library, but for simplicity, generate basic and note
            comment = "# Generated from Charonfig schema\n# Descriptions can be added manually\n"
            if format == "yaml":
                with open(output_path, "w") as f:
                    f.write(comment)
                    yaml.dump(config_dict, f, default_flow_style=False, sort_keys=False)
                print(f"YAML file generated at: {output_path} with header comment")
            else:
                with open(output_path, "w") as f:
                    f.write(comment.replace('#', '//'))  # JSON comment hack, but invalid JSON
                    json.dump(config_dict, f, indent=2)
                print(f"JSON file generated at: {output_path} (comments are invalid in JSON; use YAML for comments)")
        else:
            if format == "json":
                with open(output_path, "w") as f:
                    json.dump(config_dict, f, indent=2)
                print(f"JSON file generated at: {output_path}")
            elif format == "yaml":
                with open(output_path, "w") as f:
                    yaml.dump(config_dict, f, default_flow_style=False)
                print(f"YAML file generated at: {output_path}")
        if format not in ("env", "json", "yaml"):
            raise ValueError(f"Unsupported format: {format}")

    def get_encryption_key(self) -> Optional[bytes]:
        """Return the encryption key used for sensitive fields."""
        return self._fernet.key if self._fernet else None

    def generate_docs(self, output_path: str = "config_docs.md") -> None:
        """Generate documentation for the configuration schema in Markdown format."""
        docs = self._generate_docs_markdown()
        with open(output_path, "w", encoding='utf-8') as f:
            f.write("\n".join(docs))
        print(f"Documentation generated at: {output_path}")

    def _generate_docs_markdown(self, prefix: str = "") -> list[str]:
        """Recursively generate Markdown docs for the schema."""
        docs = []
        if not prefix:
            docs.append("# Configuration Schema Documentation\n\n")
        for name, field in self._fields.items():
            header = f"## {name}" if not prefix else f"### {prefix}{name}"
            docs.append(header)
            field_type = field.config_class.__name__ if isinstance(field, NestedField) else type(field).__name__
            docs.append(f"\n- **Type**: {field_type}\n")
            docs.append(f"- **Required**: {field.required}\n")
            if field.default is not None:
                docs.append(f"- **Default**: {repr(field.default)}\n")
            docs.append(f"- **Sensitive**: {field.sensitive}\n")
            if field.description:
                docs.append(f"- **Description**: {field.description}\n")
            docs.append("\n")
            if isinstance(field, NestedField):
                sub_prefix = f"{prefix}{name}."
                sub_instance = field.config_class(skip_initial_validation=True)
                sub_docs = sub_instance._generate_docs_markdown(sub_prefix)
                docs.extend(sub_docs)
        return docs

__version__ = "0.1.0"
__all__ = [
    "CharonfigError",
    "MissingRequiredFieldError",
    "TypeValidationError",
    "EncryptionError",
    "Field",
    "StringField",
    "IntegerField",
    "BooleanField",
    "NestedField",
    "BaseConfig",
]