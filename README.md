# Vault

> Vault 687 in Gringotts Wizarding Bank
>
> "Inside were mounds of gold coins. Columns of silver. Heaps of little bronze Knuts."
>
> -- Description of the interior of the Potter vault

## Quick Start

```
/usr/local/opt/python@3.8/bin/python3 -m venv .virtualenv
make dev
make web
```

Run job:

```
./ve python scripts/job.py user_count
```

## Production

Set environment variables, or create `.env` file:

```
FLASK_ENV=production
APP_CONFIG=/path/to/production_settings.py
```

Start WSGI server:

```
waitress-serve --port=5050 scripts.web:app
```
