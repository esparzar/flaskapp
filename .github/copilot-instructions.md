# Copilot Instructions for AI Agents

## Project Overview
This codebase is a Flask application using a Python 3.12 virtual environment (`flaskevn/`). It leverages several Flask extensions for REST APIs, authentication, migrations, CORS, and SQLAlchemy ORM. Most code is installed in `site-packages`—user app code may be outside this folder.

## Architecture & Major Components
- **Flask App**: Core logic likely resides outside `flaskevn/` (not visible in current context). Framework code is in `flaskevn/lib/python3.12/site-packages/flask/`.
- **REST API**: Uses `flask_restful` for resource routing and request parsing.
- **Database**: Managed via `flask_sqlalchemy` (ORM) and `flask_migrate` (Alembic migrations).
- **Authentication**: Provided by `flask_login`.
- **CORS**: Managed by `flask_cors`.
- **Forms**: Uses `flask_wtf` and `wtforms` for form handling and CSRF protection.

## Developer Workflows
- **Environment Activation**: Run `source flaskevn/bin/activate` to activate the Python virtual environment.
- **Run App**: Use `flask run` or `gunicorn <app_module>:app` from the project root (after activation).
- **Database Migrations**: Use `flask db init`, `flask db migrate`, and `flask db upgrade` for Alembic migrations.
- **Install Dependencies**: Use `pip install <package>` inside the virtual environment.

## Project-Specific Patterns & Conventions
- **No system site packages**: Only packages in `flaskevn` are used (`pyvenv.cfg`).
- **Sans-IO Code**: Some Flask internals (see `flask/sansio/`) are designed for compatibility with async frameworks (e.g., Quart) and avoid IO/globals.
- **Translations**: WTForms uses gettext for translations. See `wtforms/locale/README.md` for instructions on adding/updating translations.
- **Configuration**: App config may be in `config.py` or loaded via environment variables (check for `.env` usage).

## Integration Points
- **Flask Extensions**: All major features (REST, DB, Auth, CORS, Forms) are provided via Flask extensions—refer to their respective folders in `site-packages` for extension-specific APIs.
- **External Services**: Database connection details are likely configured via environment variables or config files.

## Key Files & Directories
- `flaskevn/bin/activate`: Activate the Python environment.
- `flaskevn/lib/python3.12/site-packages/`: Contains all installed packages and extensions.
- `flaskevn/pyvenv.cfg`: Python environment configuration.
- `wtforms/locale/README.md`: WTForms translation workflow.
- `flask/sansio/README.md`: Flask sans-IO design notes.

## Example Workflow
```bash
source flaskevn/bin/activate
pip install -r requirements.txt
flask db upgrade
flask run
```

## Tips for AI Agents
- Always activate the virtual environment before running Python commands.
- Use Flask CLI for migrations and app management.
- Check for `.env` or config files for environment-specific settings.
- For extension APIs, refer to their `site-packages` folders for implementation details.

---
*Update this file as new patterns or workflows emerge. Ask for feedback if any section is unclear or incomplete.*
