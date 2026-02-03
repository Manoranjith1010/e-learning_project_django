# Development Setup Instructions

## Prerequisites
- Python 3.10+
- pip and virtualenv
- PostgreSQL (optional, SQLite for development)
- Redis (optional, for caching)

## Setup Steps

### 1. Clone Repository
```bash
git clone <repository-url>
cd e-learning_project_django
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
```

Edit `.env` with your settings:
```env
DEBUG=True
SECRET_KEY=your-secret-key
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

### 5. Create Logs Directory
```bash
mkdir -p logs
```

### 6. Run Migrations
```bash
python manage.py migrate
```

### 7. Create Sample Data
```bash
python manage.py create_sample_data
```

### 8. Create Superuser
```bash
python manage.py createsuperuser
```

### 9. Run Development Server
```bash
python manage.py runserver
```

Visit: http://localhost:8000

### 10. Admin Panel
```
URL: http://localhost:8000/admin
Username: (from createsuperuser)
Password: (from createsuperuser)
```

## Docker Setup (Alternative)

### Using Docker Compose
```bash
docker-compose up -d
```

This starts:
- Django app on http://localhost:8000
- PostgreSQL on localhost:5432
- Redis on localhost:6379

### Run migrations in Docker
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py create_sample_data
```

## Common Commands

### Run Tests
```bash
pytest
pytest --cov=apps --cov=common
```

### Create Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Shell
```bash
python manage.py shell
```

### Celery (if configured)
```bash
celery -A myproject worker -l info
```

## IDE Setup

### VS Code
1. Install Python extension
2. Select interpreter: `.venv/bin/python`
3. Install pylint: `pip install pylint`

### PyCharm
1. Go to Settings → Project → Python Interpreter
2. Add interpreter from `.venv/bin/python`

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| DEBUG | True | Debug mode |
| SECRET_KEY | random | Django secret key |
| DB_ENGINE | sqlite3 | Database backend |
| EMAIL_BACKEND | console | Email backend |
| LOG_LEVEL | INFO | Logging level |

## Troubleshooting

### Port 8000 already in use
```bash
python manage.py runserver 8001
```

### Database locked
```bash
rm db.sqlite3
python manage.py migrate
```

### Cache issues
```bash
python manage.py shell
>>> from django.core.cache import cache
>>> cache.clear()
```

### Module not found
```bash
pip install -r requirements.txt
```

## Next Steps

1. Read [STRUCTURE_GUIDE.md](STRUCTURE_GUIDE.md)
2. Review [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
3. Check individual app READMEs in `apps/*/README.md`
4. Run tests: `pytest`
5. Start developing!

## Support

For issues, check:
1. Error messages in console
2. Logs in `logs/app.log`
3. Django debug toolbar
4. GitHub issues (if applicable)
