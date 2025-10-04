# Publishing to PyPI Guide

Complete guide for publishing TSDC to PyPI.

## Prerequisites

1. PyPI account: https://pypi.org/account/register/
2. TestPyPI account (optional): https://test.pypi.org/account/register/
3. Verified email address

## Step 1: Get API Token

### For PyPI (Production)

1. Go to https://pypi.org/manage/account/
2. Scroll to "API tokens"
3. Click "Add API token"
4. Name: `TSDC Upload`
5. Scope: `Entire account` (or specific project after first upload)
6. Click "Create token"
7. **Copy the token immediately** (it won't be shown again!)

### For TestPyPI (Optional, for testing)

1. Go to https://test.pypi.org/manage/account/
2. Follow same steps as above

## Step 2: Build the Package

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build
python -m build
```

Expected output:
```
Successfully built tsdc-0.1.0.tar.gz and tsdc-0.1.0-py3-none-any.whl
```

## Step 3: Check the Package

```bash
twine check dist/*
```

Expected output:
```
Checking dist/tsdc-0.1.0-py3-none-any.whl: PASSED
Checking dist/tsdc-0.1.0.tar.gz: PASSED
```

## Step 4: Upload

### Option A: Upload to TestPyPI (Recommended First)

```bash
twine upload --repository testpypi dist/*
```

Username: `__token__`
Password: `pypi-YOUR_TEST_TOKEN_HERE`

Test installation:
```bash
pip install --index-url https://test.pypi.org/simple/ tsdc
```

### Option B: Upload to PyPI (Production)

```bash
twine upload dist/*
```

Username: `__token__`
Password: `pypi-YOUR_PRODUCTION_TOKEN_HERE`

Or with token in command:
```bash
twine upload -u __token__ -p pypi-YOUR_TOKEN_HERE dist/*
```

## Step 5: Verify

After upload, check:
- https://pypi.org/project/tsdc/
- Install and test: `pip install tsdc`

## Configuration File (Optional)

Create `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_PRODUCTION_TOKEN

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TEST_TOKEN
```

Then upload without entering credentials:
```bash
twine upload dist/*
```

## Common Issues

### 1. Package already exists

**Error:** `File already exists`

**Solution:** Bump version in `setup.py` and `pyproject.toml`, rebuild

### 2. Invalid token

**Error:** `Invalid or non-existent authentication information`

**Solution:** 
- Check token is correct
- Username must be `__token__` (with double underscores)
- Token should start with `pypi-`

### 3. README rendering issues

**Error:** `The description failed to render`

**Solution:** Check README.md for valid markdown

### 4. Missing files

**Error:** Files not included in package

**Solution:** Update `MANIFEST.in`

## Version Management

Update version in both files:
1. `setup.py` → `version="0.1.1"`
2. `pyproject.toml` → `version = "0.1.1"`

Follow semantic versioning:
- `0.1.0` → `0.1.1` (patch - bug fixes)
- `0.1.0` → `0.2.0` (minor - new features, backward compatible)
- `0.1.0` → `1.0.0` (major - breaking changes)

## Publishing Checklist

- [ ] All tests passing (`pytest tests/ -v`)
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped in setup.py and pyproject.toml
- [ ] Git committed and tagged
- [ ] Built successfully (`python -m build`)
- [ ] Checked with twine (`twine check dist/*`)
- [ ] Uploaded to TestPyPI (optional)
- [ ] Tested installation from TestPyPI
- [ ] Uploaded to PyPI
- [ ] Verified on PyPI website
- [ ] Tested installation: `pip install tsdc`
- [ ] Create GitHub release

## GitHub Release (After PyPI Upload)

1. Go to https://github.com/DeepPythonist/tsdc/releases
2. Click "Create a new release"
3. Tag: `v0.1.0`
4. Title: `TSDC v0.1.0 - Initial Release`
5. Description: Copy from CHANGELOG.md
6. Attach dist files (optional)
7. Click "Publish release"

## Updating Package

1. Make changes
2. Run tests
3. Update CHANGELOG.md
4. Bump version
5. Commit changes
6. Build: `python -m build`
7. Upload: `twine upload dist/*`
8. Create GitHub release

## Security

⚠️ **Never commit API tokens!**

Add to `.gitignore`:
```
.pypirc
*.token
```

## Useful Commands

```bash
# Check package info
python setup.py --version
python setup.py --name
python setup.py --long-description

# List package contents
tar -tzf dist/tsdc-0.1.0.tar.gz
unzip -l dist/tsdc-0.1.0-py3-none-any.whl

# Test local installation
pip install dist/tsdc-0.1.0-py3-none-any.whl

# Uninstall
pip uninstall tsdc
```

## Support

For issues:
- PyPI support: https://pypi.org/help/
- TestPyPI: https://test.pypi.org/help/

---

**Ready to publish? Let's go! 🚀**
