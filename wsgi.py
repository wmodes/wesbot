# wsgi.py

from app import app

def application(environ, start_response):
    """WSGI application."""

    return app(environ, start_response)

