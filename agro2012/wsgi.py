"""
WSGI config for agroholding2012 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from osenv import osenv

from django.core.wsgi import get_wsgi_application

osenv = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agro2012.dev_settings")
#osenv

application = get_wsgi_application()
