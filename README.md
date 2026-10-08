# Pytest API Framework

Small pytest-based API test framework for GoRest endpoints.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configuration

The default environment is configured in `config/endpoint.json`.
You can override it from the command line:

```powershell
pytest --host prod
```

Authenticated create-user tests need a GoRest token:

```powershell
$env:GOREST_TOKEN = "your-token-here"
pytest
```

Do not commit `.env`, local virtual environments, IDE settings, logs, or pytest caches.
