# Security Guide - Environment Variables Setup

## 🔐 Protecting Sensitive Information

This guide explains how to securely manage credentials and API tokens in the camera-master project.

## Environment Variables

### Required Variables

- `PYPI_API_TOKEN` - Your PyPI API token for package deployment
- `PYPI_USERNAME` - (Optional) Defaults to `__token__` if not set

## Setup Instructions

### Windows (PowerShell)

#### Temporary (Current Session Only)
```powershell
$env:PYPI_API_TOKEN="your-actual-token-here"
```

#### Permanent (User Level)
```powershell
[System.Environment]::SetEnvironmentVariable('PYPI_API_TOKEN', 'your-token-here', 'User')
```

#### Verify
```powershell
echo $env:PYPI_API_TOKEN
```

### Windows (CMD)

#### Temporary
```cmd
set PYPI_API_TOKEN=your-token-here
```

#### Permanent
```cmd
setx PYPI_API_TOKEN "your-token-here"
```

### Linux/Mac (Bash)

#### Temporary
```bash
export PYPI_API_TOKEN="your-token-here"
```

#### Permanent (add to ~/.bashrc or ~/.zshrc)
```bash
echo 'export PYPI_API_TOKEN="your-token-here"' >> ~/.bashrc
source ~/.bashrc
```

## Using .env File (Optional)

### 1. Copy the template
```bash
cp .env.example .env
```

### 2. Edit .env with your credentials
```bash
PYPI_USERNAME=__token__
PYPI_API_TOKEN=your-actual-token-here
```

### 3. Load in PowerShell (if needed)
```powershell
Get-Content .env | ForEach-Object {
    if ($_ -match '^([^=]+)=(.*)$') {
        [System.Environment]::SetEnvironmentVariable($matches[1], $matches[2])
    }
}
```

## 🚨 Security Checklist

- ✅ `.env` is in `.gitignore` - **NEVER commit it!**
- ✅ Use `.env.example` as template (no real credentials)
- ✅ Rotate tokens regularly
- ✅ Use environment variables instead of hardcoding
- ✅ Never share tokens in documentation or commits

## Getting Your PyPI Token

1. Go to https://pypi.org/manage/account/token/
2. Login to your PyPI account
3. Create a new API token
4. Set scope (entire account or specific project)
5. Copy the token (starts with `pypi-`)
6. Store it securely as environment variable

## Deployment

Once environment variables are set:

```powershell
# Build and deploy
.\deploy.ps1
```

The script will automatically use `$env:PYPI_API_TOKEN` from your environment.

## Troubleshooting

### Error: "PYPI_API_TOKEN environment variable not set"

**Solution:** Set the environment variable before running deployment:
```powershell
$env:PYPI_API_TOKEN="your-token-here"
.\deploy.ps1
```

### Token not persisting after restart

**Solution:** Set it permanently:
```powershell
[System.Environment]::SetEnvironmentVariable('PYPI_API_TOKEN', 'your-token', 'User')
```
Then restart PowerShell.

## Best Practices

1. **Never commit secrets** - Always use environment variables
2. **Use token authentication** - More secure than username/password
3. **Limit token scope** - Create project-specific tokens
4. **Rotate tokens regularly** - Change tokens every few months
5. **Use .env for local dev** - But never commit the .env file
6. **Use secrets management** - For production, use tools like Azure Key Vault, AWS Secrets Manager, or GitHub Secrets

## Additional Resources

- [PyPI API Tokens Documentation](https://pypi.org/help/#apitoken)
- [Twelve-Factor App: Config](https://12factor.net/config)
- [GitHub: Removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
