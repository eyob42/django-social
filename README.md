# django-social

A small Django social app (dwitter-like) that demonstrates user profiles and short "dweets" (posts).

This repository contains a Django project with a `dwitter` app and the project package `social`.

## Features

- User profiles
- Create and view short posts (dweets)
- Basic templates for dashboard and profile pages
- SQLite backend (default)

## Requirements

- Python 3.8+ (use the version installed on your system)
- Django (the project was built with Django; if there's no `requirements.txt`, install Django directly)

## Quick setup (Windows PowerShell)

Open PowerShell in the repository root and run:

```powershell
# create virtual environment
python -m venv .\venv
# activate the venv
.\venv\Scripts\Activate.ps1

# install dependencies (if requirements.txt exists)
if (Test-Path requirements.txt) { pip install -r requirements.txt } else { pip install Django }

# apply migrations
python manage.py migrate

# create an admin user (optional)
python manage.py createsuperuser

# run the dev server
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.


## Project structure

Top-level files and folders (important ones):

- `manage.py` - Django management script
- `db.sqlite3` - default SQLite database (created after migrations)
- `social/` - Django project package (settings, URLs, WSGI/ASGI)
- `dwitter/` - application implementing the social/dweet features
  - `models.py`, `views.py`, `forms.py`, `templates/` and `migrations/`

Example template files are included under `dwitter/templates/dwitter/` (dashboard, profile list, profile).

## Notes

- The project uses SQLite by default, which requires no extra configuration for local development.
- If you add environment-specific secrets or use a different database, update `social/settings.py` accordingly.

## Contributing

Contributions are welcome. Open an issue to discuss larger changes or submit a PR with a clear description of the change.




