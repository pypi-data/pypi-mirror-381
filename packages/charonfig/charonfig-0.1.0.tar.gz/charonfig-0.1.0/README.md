# README.md
# Charonfig

A flexible Python configuration management library that supports typed fields, environment variable loading, nested configurations, encryption for sensitive data, and export to multiple formats (ENV, JSON, YAML). It uses a declarative schema approach for validation and documentation generation.

## Features

- **Typed Fields**: Define string, integer, boolean, and nested config fields with validation.
- **Environment Loading**: Automatically load from env vars with prefix support.
- **Encryption**: Fernet-based encryption for sensitive fields.
- **Export Formats**: Generate .env, JSON, or YAML files with optional comments.
- **Documentation**: Auto-generate Markdown docs from schema.
- **Nested Configs**: Support for hierarchical configurations.
- **CLI Tool**: Command-line interface for generating, validating, and documenting configs.

## Installation

```bash
pip install charonfig