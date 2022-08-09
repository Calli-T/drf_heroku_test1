import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytodo.settings')

application = get_wsgi_application()


from whitenoise import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
