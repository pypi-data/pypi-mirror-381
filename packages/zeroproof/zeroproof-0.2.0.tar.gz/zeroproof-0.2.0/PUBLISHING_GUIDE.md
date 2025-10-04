# Publishing Guide for ZeroProof Python SDK

This guide covers how to build and publish the ZeroProof Python SDK to PyPI using `uv`.

## Prerequisites

1. **Install uv**: Make sure you have `uv` installed
   ```bash
   pip install uv
   ```

2. **PyPI Account**: Create an account at https://pypi.org

3. **PyPI API Token**: Generate an API token at https://pypi.org/manage/account/token/
   - Create a token scoped to the `zeroproof` project (after first upload, you can create project-specific tokens)
   - Store it securely (you'll only see it once)

## Building the Package

### 1. Update Version (if needed)

Use `uv version` to update the package version:

```bash
cd python-sdk

# Update to a specific version
uv version 0.2.1

# Or bump version semantically
uv version --bump patch   # 0.2.0 -> 0.2.1
uv version --bump minor   # 0.2.0 -> 0.3.0
uv version --bump major   # 0.2.0 -> 1.0.0
```

### 2. Build the Package

Build both source distribution and wheel:

```bash
cd python-sdk
uv build
```

This creates:
- `dist/zeroproof-0.2.0.tar.gz` (source distribution)
- `dist/zeroproof-0.2.0-py3-none-any.whl` (wheel)

### 3. Verify the Build

Test that the package can be imported:

```bash
# Test with the wheel
uv run --with ./dist/zeroproof-0.2.0-py3-none-any.whl --no-project -- python -c "import zeroproof; print(f'Version: {zeroproof.__version__}')"
```

## Publishing to PyPI

### Option 1: Publish to Test PyPI (Recommended First)

Test PyPI is a separate instance of PyPI for testing package uploads.

1. **Create TestPyPI account**: https://test.pypi.org/account/register/

2. **Get TestPyPI token**: https://test.pypi.org/manage/account/token/

3. **Publish to TestPyPI**:
   ```bash
   cd python-sdk
   
   # Set your TestPyPI token
   $env:UV_PUBLISH_TOKEN = "pypi-your-testpypi-token-here"
   
   # Publish
   uv publish --index testpypi
   ```

4. **Test installation from TestPyPI**:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --no-deps zeroproof
   ```

### Option 2: Publish to Production PyPI

Once you've tested on TestPyPI:

```bash
cd python-sdk

# Set your PyPI token
$env:UV_PUBLISH_TOKEN = "pypi-your-production-token-here"

# Publish
uv publish
```

Or provide the token directly:

```bash
uv publish --token pypi-your-token-here
```

### Using a Custom Index

If you have a custom package index configured in `pyproject.toml`:

```toml
[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
publish-url = "https://test.pypi.org/legacy/"
explicit = true
```

Then publish with:

```bash
uv publish --index testpypi
```

## Troubleshooting

### Issue: "File already exists"

If you get an error about files already existing:

1. **Increment the version**: PyPI doesn't allow re-uploading the same version
   ```bash
   uv version --bump patch
   uv build
   uv publish
   ```

2. **Or use TestPyPI** for testing different builds of the same version

### Issue: Upload interrupted

If the upload fails partway through:

```bash
# Retry with the same command - uv will skip already-uploaded files
uv publish

# Or use --check-url to verify existing files
uv publish --check-url https://pypi.org/simple/
```

### Issue: Authentication failed

- Verify your token starts with `pypi-`
- Make sure you're using the correct token for the target (TestPyPI vs PyPI)
- Tokens are different for each service

## Publishing from CI/CD

### GitHub Actions Example

Add this to `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      id-token: write  # For trusted publishing
      contents: read
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install uv
        run: pip install uv
      
      - name: Build package
        run: |
          cd python-sdk
          uv build
      
      - name: Publish to PyPI
        run: |
          cd python-sdk
          uv publish
        env:
          UV_PUBLISH_TOKEN: ${{ secrets.PYPI_API_TOKEN }}
```

### Using Trusted Publishers (Recommended)

For GitHub Actions, you can use PyPI's Trusted Publishers feature (no token needed):

1. Go to https://pypi.org/manage/project/zeroproof/settings/publishing/
2. Add GitHub as a trusted publisher
3. Provide your GitHub organization/username and workflow details
4. In GitHub Actions, just run `uv publish` without setting UV_PUBLISH_TOKEN

## Post-Publishing Checklist

After publishing:

- [ ] Verify package appears on PyPI: https://pypi.org/project/zeroproof/
- [ ] Test installation: `pip install zeroproof`
- [ ] Test import: `python -c "import zeroproof; print(zeroproof.__version__)"`
- [ ] Update GitHub release notes
- [ ] Update documentation if needed
- [ ] Announce on relevant channels

## Version Numbering Guidelines

Follow Semantic Versioning (SemVer):

- **Patch** (0.2.0 -> 0.2.1): Bug fixes, minor changes
- **Minor** (0.2.0 -> 0.3.0): New features, backward compatible
- **Major** (0.2.0 -> 1.0.0): Breaking changes

For pre-releases:
```bash
uv version --bump minor --bump alpha  # 0.2.0 -> 0.3.0a1
uv version --bump beta                # 0.3.0a1 -> 0.3.0b1
uv version --bump rc                  # 0.3.0b1 -> 0.3.0rc1
uv version --bump stable              # 0.3.0rc1 -> 0.3.0
```

## Security Best Practices

1. **Never commit tokens**: Add to `.gitignore`:
   ```
   .pypirc
   *.token
   ```

2. **Use project-scoped tokens**: Limit token permissions to specific projects

3. **Rotate tokens regularly**: Generate new tokens periodically

4. **Use environment variables**: Don't hardcode tokens in scripts
   ```bash
   $env:UV_PUBLISH_TOKEN = "pypi-token"  # PowerShell
   export UV_PUBLISH_TOKEN="pypi-token"   # Bash
   ```

## Quick Reference

```bash
# Common workflow
cd python-sdk

# 1. Update version
uv version --bump patch

# 2. Build
uv build

# 3. Test locally
uv run --with ./dist/zeroproof-*.whl --no-project -- python -c "import zeroproof"

# 4. Publish to TestPyPI first
uv publish --index testpypi --token $UV_PUBLISH_TOKEN

# 5. Publish to PyPI
uv publish --token $UV_PUBLISH_TOKEN
```

## Resources

- **uv documentation**: https://docs.astral.sh/uv/
- **PyPI Help**: https://pypi.org/help/
- **TestPyPI**: https://test.pypi.org/
- **Trusted Publishers**: https://docs.pypi.org/trusted-publishers/
- **Semantic Versioning**: https://semver.org/

## Getting Help

If you encounter issues:

1. Check the [uv documentation](https://docs.astral.sh/uv/guides/publish/)
2. Review PyPI's [publishing guide](https://packaging.python.org/tutorials/packaging-projects/)
3. Open an issue on the ZeroProof repository

---

**Last Updated**: October 3, 2025
