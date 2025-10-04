# MCP Registry Publishing Guide

This document outlines how to publish the SQLite MCP Server to the [MCP Registry](https://registry.modelcontextprotocol.io/).

## 📋 Overview

The SQLite MCP Server is configured for **hybrid deployment** with multiple package types:

- **PyPI Package**: `mcp-server-sqlite` v2.6.0
- **Docker Image**: `writenotenow/sqlite-mcp-server` v2.6.0

## 🔧 Prerequisites Setup

### Required Secrets (for automated publishing)

Add these secrets to your GitHub repository (Settings → Secrets and variables → Actions):

1. **`PYPI_TOKEN`** - PyPI API token for publishing Python packages
2. **`DOCKERHUB_USERNAME`** - Your Docker Hub username (`writenotenow`)
3. **`DOCKERHUB_TOKEN`** - Docker Hub access token

### Package Validation Requirements

The MCP Registry validates package ownership through these mechanisms:

#### ✅ PyPI Validation
- **Requirement**: README must contain `mcp-name: io.github.neverinfamous/sqlite-mcp-server`
- **Status**: ✅ Added to README.md (line 13, HTML comment)
- **Verification**: Registry checks PyPI package description for this string

#### ✅ Docker Validation  
- **Requirement**: Docker image must have label `io.modelcontextprotocol.server.name="io.github.neverinfamous/sqlite-mcp-server"`
- **Status**: ✅ Added to Dockerfile (line 28)
- **Verification**: Registry inspects Docker image manifest for this label

## 🚀 Automated Publishing (Recommended)

### GitHub Actions Workflow

The repository includes `.github/workflows/publish-mcp.yml` which automatically:

1. **Triggers** on version tags (e.g., `v2.6.0`) or manual dispatch
2. **Tests** the package with quick test suite
3. **Publishes** to PyPI using `uv publish`
4. **Builds** and pushes Docker image to Docker Hub
5. **Publishes** to MCP Registry using GitHub OIDC authentication

### To Publish a New Version

1. **Update version** in `pyproject.toml` and `server.json`
2. **Commit changes** and push to main branch
3. **Create and push version tag**:
   ```bash
   git tag v2.6.1
   git push origin v2.6.1
   ```
4. **Monitor workflow** in GitHub Actions tab

## 🛠️ Manual Publishing (Alternative)

### Step 1: Install MCP Publisher CLI

```bash
# macOS/Linux with Homebrew
brew install mcp-publisher

# Or download binary directly
curl -L "https://github.com/modelcontextprotocol/registry/releases/download/v1.0.0/mcp-publisher_1.0.0_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/').tar.gz" | tar xz mcp-publisher
```

### Step 2: Authenticate with GitHub

```bash
mcp-publisher login github
```

This opens your browser for OAuth authentication with your GitHub account.

### Step 3: Validate Configuration

```bash
# Validate server.json against schema
python3 validate_server_json.py

# Expected output: ✅ server.json is valid against the MCP schema!
```

### Step 4: Publish to Registry

```bash
mcp-publisher publish
```

### Step 5: Verify Publication

```bash
curl "https://registry.modelcontextprotocol.io/v0/servers?search=io.github.neverinfamous/sqlite-mcp-server" | jq .
```

## 📊 Package Status

### PyPI Package: `mcp-server-sqlite`
- **Current Version**: 2.6.0
- **Registry**: https://pypi.org/project/mcp-server-sqlite/
- **Installation**: `pip install mcp-server-sqlite`
- **MCP Name**: Added to README.md for validation

### Docker Image: `writenotenow/sqlite-mcp-server`
- **Current Version**: v2.6.0, latest
- **Registry**: https://hub.docker.com/r/writenotenow/sqlite-mcp-server
- **Usage**: `docker run writenotenow/sqlite-mcp-server --db-path /path/to/db.sqlite`
- **MCP Label**: Added to Dockerfile for validation

## 🔍 Validation Details

The `server.json` configuration includes:

```json
{
  "name": "io.github.neverinfamous/sqlite-mcp-server",
  "version": "2.6.0",
  "packages": [
    {
      "registryType": "pypi",
      "identifier": "mcp-server-sqlite",
      "version": "2.6.0"
    },
    {
      "registryType": "oci", 
      "registryBaseUrl": "https://docker.io",
      "identifier": "writenotenow/sqlite-mcp-server",
      "version": "v2.6.0"
    }
  ]
}
```

## 🐛 Troubleshooting

### Common Issues

**"Package validation failed"**
- Verify PyPI package contains MCP name in README
- Verify Docker image has correct label
- Check package versions match server.json

**"Authentication failed"**  
- Ensure you're logged into correct GitHub account
- Verify GitHub account has access to repository
- Try re-authenticating: `mcp-publisher login github`

**"Namespace not authorized"**
- Namespace `io.github.neverinfamous/*` requires GitHub authentication
- Ensure authenticated user matches GitHub username in namespace

### Verification Commands

```bash
# Check PyPI package
curl -s https://pypi.org/pypi/mcp-server-sqlite/json | jq '.info.description' | grep -o 'mcp-name: [^"]*'

# Check Docker image labels
docker inspect writenotenow/sqlite-mcp-server:latest | jq '.[0].Config.Labels'

# Validate server.json
python3 validate_server_json.py
```

## 📚 Additional Resources

- [MCP Registry Publishing Guide](https://github.com/modelcontextprotocol/registry/blob/main/docs/guides/publishing/publish-server.md)
- [GitHub Actions Automation](https://github.com/modelcontextprotocol/registry/blob/main/docs/guides/publishing/github-actions.md)
- [Server.json Schema](https://static.modelcontextprotocol.io/schemas/2025-09-16/server.schema.json)
- [MCP Registry](https://registry.modelcontextprotocol.io/)

---

*This guide ensures the SQLite MCP Server is properly published and discoverable in the MCP Registry for users worldwide.*
