from pathlib import Path
import os
import dj_database_url

if os.path.isfile('env.py'):
    import env

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Security
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_secret_key')
DEBUG = True
ALLOWED_HOSTS = [
    'newssite.herokuapp.com',
    'localhost',
    'reddit-new-2d2861630b68.herokuapp.com',
    '127.0.0.1',
    '8000-markmcl25-project41-o0vfyfnhrqc.ws-eu116.gitpod.io',
    '8000-markmcl25-project41-zpk274etwsj.ws-eu117.gitpod.io',
]

ROOT_URLCONF = 'newssite.urls'

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'https://8000-markmcl25-project41-o0vfyfnhrqc.ws-eu116.gitpod.io',
    'https://8000-markmcl25-project41-zpk274etwsj.ws-eu117.gitpod.io',
    'https://newssite.herokuapp.com',
    'https://reddit-new-2d2861630b68.herokuapp.com',
]

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'crispy_forms',
    'crispy_bootstrap4',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'cloudinary',
    'django_summernote',
    'reddit',
]

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# Database
DATABASES = {
    'default': dj_database_url.config(default=f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}')
}

# Static Files
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default Primary Key Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login and Allauth
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/logged_out/'
LOGIN_URL = 'accounts/login/'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_USERNAME_REQUIRED = True