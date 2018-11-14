"""
WSGI config for accounting project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accounting.settings');

sys.stdout = sys.stderr

DEBUG = True

application = get_wsgi_application()
