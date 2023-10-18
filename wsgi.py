"""
wsgi.py - WSGI Application Entry Point

This file serves as the entry point for the WSGI application. It imports the 'app' object from the 'app' module and defines the 'application' function required by the WSGI specification.

Author: Wes Modes
Date: 2023
"""

from app import app

def application(environ, start_response):
    """WSGI application."""

    return app(environ, start_response)

