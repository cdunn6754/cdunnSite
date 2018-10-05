import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_URL = '/static/'

STATIC_ROOT = '/static/'

## Media files
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "/media/"

## Security Settings

# Prevent browser from MIME sniffing, lock content type header
SECURE_CONTENT_TYPE_NOSNIFF = False

# turn on xss attack filtering
SECURE_BROWSER_XSS_FILTER = False

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

X_FRAME_OPTIONS = 'DENY'

# Nginx is configured to reroute to HTTPS
SECURE_SSL_REDIRECT = False
