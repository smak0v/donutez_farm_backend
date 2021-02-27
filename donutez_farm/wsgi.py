"""
WSGI config for donutez_farm project
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'donutez_farm.settings')

application = get_wsgi_application()
