"""
WSGI config for vunderink project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vunderink.settings')

application = get_wsgi_application()


project_folder = os.path.expanduser('/Users/jordanhillman/Desktop/laurenvunderink/vunderink')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
