# Versioning Schema

This document outlines the versioning schema used for the statflow package.

## Version Format

The version format follows Semantic Versioning (SemVer) principles with a three-part version number:

```text
MAJOR.MINOR.PATCH
```

- **MAJOR**: Incremented when making incompatible API changes
- **MINOR**: Incremented when adding functionality in a backward-compatible manner
- **PATCH**: Incremented when making backward-compatible bug fixes

## Current Versioning History

The versioning history of statflow follows this pattern:

- **v2.1.0**: Initial Release (2024-10-28)
  - First public release with core functionality

- **v3.0.0**: Major Update (2024-11-04)
  - Significant changes to the API structure
  - Removal of deprecated modules

- **v3.0.6**: Minor Update (2025-02-03)
  - Term replacements for better clarity
  - Improved documentation

- **v3.1.0**: Feature Update (2025-04-05)
  - Enhanced variable naming conventions
  - Improved code readability and maintainability
  - Added new parameters for better control

## Versioning Notes

- The project started at version 2.1.0 rather than 0.1.0 due to the initial development phase being completed before proper versioning was implemented.
- Future versions will continue to follow the SemVer principles, with appropriate increments based on the nature of changes.
- Each release is documented in the CHANGELOG.md file with detailed information about the changes made.

## Release Process

1. **Development**: Changes are made in the development branch
2. **Testing**: Changes are tested thoroughly
3. **Version Update**: The version number is updated in the CHANGELOG.md and other relevant files
4. **Release**: The new version is tagged and released
5. **Documentation**: The CHANGELOG.md is updated with details about the changes

## Version Indicators in Code

The version of the package is defined in the `__init__.py` file and can be accessed programmatically:

```python
import statflow
print(statflow.__version__)
```
