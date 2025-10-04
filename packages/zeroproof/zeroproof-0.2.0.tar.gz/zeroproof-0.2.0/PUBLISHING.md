# Publishing to PyPI

This guide covers how to publish the ZeroProof Python SDK to PyPI.

## Prerequisites

1. **PyPI Account**: Create an account at [https://pypi.org](https://pypi.org)
2. **Test PyPI Account** (recommended): Create an account at [https://test.pypi.org](https://test.pypi.org)
3. **API Token**: Generate an API token from your PyPI account settings

## Installation for Development

```bash
cd python-sdk

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```

## Testing Locally

### 1. Test the SDK

```bash
# Set your API key
export ZEROPROOF_API_KEY="zkp_your_actual_key"  # macOS/Linux
# OR
set ZEROPROOF_API_KEY=zkp_your_actual_key       # Windows

# Run the example
python examples/shopping_agent_demo.py
```

### 2. Run Code Quality Checks

```bash
# Format code
black zeroproof/

# Check linting
flake8 zeroproof/

# Type checking
mypy zeroproof/
```

## Building the Package

### 1. Clean Previous Builds

```bash
rm -rf build/ dist/ *.egg-info
```

### 2. Build Distribution Files

```bash
# Install build tools
pip install build twine

# Build the package
python -m build
```

This creates:
- `dist/zeroproof-0.1.0.tar.gz` (source distribution)
- `dist/zeroproof-0.1.0-py3-none-any.whl` (wheel distribution)

### 3. Check Package

```bash
# Verify the package is well-formed
twine check dist/*
```

## Publishing

### Test PyPI (Recommended First)

Test your package on Test PyPI before publishing to the real PyPI:

```bash
# Upload to Test PyPI
twine upload --repository testpypi dist/*

# Enter your Test PyPI credentials or API token
```

Then test installation:

```bash
# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ zeroproof

# Test it works
python -c "from zeroproof import ZeroProof; print('Success!')"
```

### Production PyPI

Once you've verified everything works on Test PyPI:

```bash
# Upload to PyPI
twine upload dist/*

# Enter your PyPI credentials or API token
```

## Using API Tokens

### Create .pypirc File

Create `~/.pypirc` (Linux/macOS) or `%USERPROFILE%\.pypirc` (Windows):

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmc...your-token-here

[testpypi]
username = __token__
password = pypi-AgENdGVzdC5weXBp...your-token-here
```

**Important**: Add `.pypirc` to your `.gitignore`!

## Version Management

Update version in three places:

1. `zeroproof/__init__.py` - `__version__ = "0.1.1"`
2. `setup.py` - `version="0.1.1"`
3. `pyproject.toml` - `version = "0.1.1"`

Consider using `setuptools_scm` for automatic versioning from git tags.

## Release Checklist

Before publishing a new version:

- [ ] Update version number in all files
- [ ] Update CHANGELOG in README.md
- [ ] Run all tests
- [ ] Run code quality checks (black, flake8, mypy)
- [ ] Build the package
- [ ] Test on Test PyPI
- [ ] Tag the release in git: `git tag v0.1.1`
- [ ] Push tags: `git push --tags`
- [ ] Publish to PyPI
- [ ] Create GitHub release with release notes

## Automated Publishing (Optional)

You can automate PyPI publishing using GitHub Actions. Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build twine
      - name: Build package
        run: python -m build
      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*
```

Add your PyPI API token as a GitHub secret named `PYPI_API_TOKEN`.

## Common Issues

### "File already exists" Error

You can't re-upload the same version. Increment the version number.

### Import Errors After Publishing

Make sure `MANIFEST.in` includes all necessary files and `setup.py` correctly specifies packages.

### Missing Dependencies

Ensure all dependencies are listed in both `setup.py` and `pyproject.toml`.

## Support

For issues with publishing, check:
- [Python Packaging Guide](https://packaging.python.org/)
- [PyPI Help](https://pypi.org/help/)
- [Twine Documentation](https://twine.readthedocs.io/)
