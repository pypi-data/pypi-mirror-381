# Publishing with GitHub Actions (Trusted Publisher)

This guide shows how to automatically publish TSDC to PyPI using GitHub Actions with Trusted Publishers (OIDC).

## Why Trusted Publishers?

✅ **More secure** - No API tokens to manage
✅ **Automatic** - Publish on every release
✅ **Simple** - No secrets to configure
✅ **Recommended** - PyPI's official recommendation

## Setup Steps

### Step 1: Configure PyPI Trusted Publisher

1. Go to https://pypi.org/manage/account/publishing/
2. Scroll to "Add a new pending publisher"
3. Fill in the form:

```
PyPI Project Name: tsdc
Owner: DeepPythonist
Repository name: tsdc
Workflow name: publish.yml
Environment name: pypi
```

4. Click "Add"

**Note:** You can set this up BEFORE the project exists on PyPI!

### Step 2: Create GitHub Environment (Optional but Recommended)

1. Go to your repository: https://github.com/DeepPythonist/tsdc
2. Click `Settings` → `Environments`
3. Click "New environment"
4. Name: `pypi`
5. Add protection rules (optional):
   - Required reviewers (for manual approval)
   - Wait timer
   - Deployment branches (only from `main`)

### Step 3: Push the Workflow Files

The workflow files are already in `.github/workflows/`:
- `publish.yml` - Publishes to PyPI on release
- `tests.yml` - Runs tests on every push

Just commit and push:

```bash
git add .github/workflows/
git commit -m "Add GitHub Actions workflows"
git push
```

### Step 4: Create a Release

#### Option A: Via GitHub Web Interface

1. Go to https://github.com/DeepPythonist/tsdc/releases
2. Click "Create a new release"
3. Click "Choose a tag" → Type `v0.1.0` → Click "Create new tag"
4. Release title: `v0.1.0 - Initial Release`
5. Description: Copy from CHANGELOG.md
6. Click "Publish release"

#### Option B: Via Command Line

```bash
# Tag the release
git tag v0.1.0
git push origin v0.1.0

# Or use GitHub CLI
gh release create v0.1.0 \
  --title "v0.1.0 - Initial Release" \
  --notes "First stable release of TSDC"
```

### Step 5: Watch the Magic ✨

After creating the release:
1. GitHub Actions will automatically trigger
2. Build the package
3. Publish to PyPI using Trusted Publisher
4. Package will be available at: https://pypi.org/project/tsdc/

## Workflow Details

### publish.yml

```yaml
Trigger: On release creation
Steps:
  1. Build the package (wheel + sdist)
  2. Upload artifacts
  3. Publish to PyPI using OIDC
```

### tests.yml

```yaml
Trigger: On push/PR to main
Matrix: Python 3.8, 3.9, 3.10, 3.11, 3.12
Steps:
  1. Install dependencies
  2. Run pytest
```

## Updating the Package

1. Make your changes
2. Update version in `setup.py` and `pyproject.toml`
3. Update `CHANGELOG.md`
4. Commit and push
5. Create a new release (e.g., `v0.1.1`)
6. GitHub Actions will automatically publish

## Manual Publish (Workflow Dispatch)

You can also manually trigger the publish workflow:

1. Go to https://github.com/DeepPythonist/tsdc/actions
2. Click "Publish to PyPI"
3. Click "Run workflow"
4. Select branch
5. Click "Run workflow"

## Troubleshooting

### Error: "Trusted publisher not configured"

- Make sure you've added the pending publisher on PyPI
- Check that Owner, Repository, and Workflow name match exactly

### Error: "OIDC token verification failed"

- Make sure the environment name matches (should be `pypi`)
- Check that `id-token: write` permission is set

### Error: "File already exists"

- Version already published
- Bump version in `setup.py` and `pyproject.toml`

### Workflow doesn't trigger

- Make sure you created a "release", not just a tag
- Check workflow file is in `.github/workflows/`

## Security Benefits

✅ **No secrets exposed** - Uses OpenID Connect
✅ **Short-lived tokens** - Automatically generated per job
✅ **Scoped permissions** - Only for this specific package
✅ **Audit trail** - All publishes logged in GitHub Actions

## Status Badge

Add to README.md:

```markdown
[![PyPI version](https://badge.fury.io/py/tsdc.svg)](https://badge.fury.io/py/tsdc)
[![Tests](https://github.com/DeepPythonist/tsdc/actions/workflows/tests.yml/badge.svg)](https://github.com/DeepPythonist/tsdc/actions/workflows/tests.yml)
```

## Additional Resources

- [PyPI Trusted Publishers Guide](https://docs.pypi.org/trusted-publishers/)
- [GitHub Actions OIDC](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish)

---

**Ready? Create your first release and watch it publish automatically! 🚀**
