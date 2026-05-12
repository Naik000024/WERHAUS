"""
Vercel Serverless Function Handler for Django.
This wraps the Django WSGI application so Vercel can run it
as a serverless Python function.
"""
import os
import sys

# Ensure the project root (warehouse_config/) is on the Python path
# so that Django apps (order, user) and settings can be imported.
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_config.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
