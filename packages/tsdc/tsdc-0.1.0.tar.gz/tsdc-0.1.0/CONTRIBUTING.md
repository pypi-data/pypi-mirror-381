# Contributing to TSDC

Thank you for your interest in contributing to TSDC! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful and inclusive. We welcome contributions from everyone.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear title and description
- Steps to reproduce the issue
- Expected vs actual behavior
- Your environment (Python version, OS, etc.)
- Code snippet if applicable

### Suggesting Features

We welcome feature suggestions! Please open an issue with:
- Clear description of the feature
- Use case and benefits
- Example usage code if possible

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Update documentation as needed
7. Submit a pull request

## Development Setup

```bash
git clone https://github.com/DeepPythonist/tsdc.git
cd tsdc
pip install -e ".[dev]"
```

## Running Tests

```bash
pytest tests/ -v
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small
- No comments in code
- Write in English only

Format your code:
```bash
black tsdc/
flake8 tsdc/
```

## Testing Guidelines

- Write tests for all new features
- Ensure existing tests pass
- Aim for high code coverage
- Test edge cases

## Documentation

- Update README.md if needed
- Add docstrings to new functions/classes
- Include usage examples
- Keep documentation clear and concise

## Project Structure

```
tsdc/
├── tsdc/              # Main library code
│   ├── core/         # Core functionality
│   ├── loaders/      # Data loaders
│   └── utils/        # Utility functions
├── examples/         # Usage examples
└── tests/           # Test suite
```

## Adding New Features

### Adding a New Loader

1. Create a new file in `tsdc/loaders/`
2. Inherit from `BaseLoader`
3. Implement required methods
4. Add tests
5. Update documentation

Example:
```python
from .base import BaseLoader

class MyLoader(BaseLoader):
    def load(self, *args, **kwargs):
        pass
    
    def validate(self, data):
        pass
```

### Adding New Preprocessing Methods

1. Add method to `Preprocessor` class
2. Update `__init__` parameters if needed
3. Add tests
4. Document the new method

## Commit Messages

Use clear, descriptive commit messages:
- Use present tense ("Add feature" not "Added feature")
- Keep first line under 50 characters
- Add detailed description if needed

Good examples:
```
Add support for irregular time series
Fix memory leak in Sequencer
Update documentation for Preprocessor
```

## Release Process

1. Update version in `setup.py`
2. Update CHANGELOG.md
3. Create a new release on GitHub
4. Tag the release

## Questions?

If you have questions, feel free to:
- Open an issue
- Check existing documentation
- Review example code

Thank you for contributing!
