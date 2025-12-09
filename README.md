# Thinkly

A minimal Django web app for sharing thoughts, inspired by the provided UI mock. Users can register, login, post thoughts with optional photos, like posts, and add comments.

## Quick start
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
```

Visit http://127.0.0.1:8000/feed/ to see the feed.

## Deployment (Render)
The `render.yaml` is prefilled for a simple Python web service using Gunicorn.

