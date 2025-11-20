"""
Django settings for feedtracker project.
"""

from decouple import config
from pathlib import Path

# Base
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# STATIC FILES / WHITENOISE
# -----------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -----------------------
# SECURITY
# -----------------------
SECRET_KEY = 'django-insecure-)+z4qi@i3m@9%3r(=-#tfi^5k&4bgf(u9vxu1v4hy$+iir*1@q'

DEBUG = True   # recuerda poner en False en producción



# -----------------------
# CORS
# -----------------------
INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
    'api',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
]
CORS_ALLOWED_ORIGINS = [
    "https://preguntas-steel.vercel.app",
    "https://preguntas-git-main-erick949s-projects.vercel.app",
    "https://preguntas-cf3zym76n-erick949s-projects.vercel.app",
    "https://preguntas-erick949s-projects.vercel.app",
    "http://localhost:5173",
]

CORS_ALLOW_CREDENTIALS = True

ALLOWED_HOSTS = [
    "*",
    "preguntas-steel.vercel.app",
    "preguntas-git-main-erick949s-projects.vercel.app",
    "preguntas-cf3zym76n-erick949s-projects.vercel.app",
    "preguntas-erick949s-projects.vercel.app",
]


# -----------------------
# MIDDLEWARE
# -----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'feedtracker.urls'

# -----------------------
# TEMPLATES
# -----------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'feedtracker.wsgi.application'

# -----------------------
# DATABASE
# -----------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# -----------------------
# PASSWORDS
# -----------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------
# INTERNATIONALIZATION
# -----------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default PK
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
