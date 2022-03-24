import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_URLCONF = 'comtrack.urls'

WSGI_APPLICATION = 'comtrack.wsgi.application'
