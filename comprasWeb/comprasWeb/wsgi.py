"""
WSGI config for comprasWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

#Enlazar configuraciones del project

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comprasWeb.settings.local') #en esta seccion se enlaza especificamente 

# application = get_wsgi_application()


from dj_static import Cling

application = Cling(get_wsgi_application())