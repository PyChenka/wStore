import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-h(q=eegta7mhi7y56r^j(o190&%cgzbu6liw1&-5#kcxhvfyn7'

DEBUG = True

ALLOWED_HOSTS = [
    # '127.0.0.1'
]

INTERNAL_IPS = [
    '127.0.0.1',
]

CACHES = {
    'default':
        {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': BASE_DIR / 'cache'
        }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'blog.apps.BlogConfig',
    'shop.apps.ShopConfig',
    'users.apps.UsersConfig',
    'contact.apps.ContactConfig',
    'search.apps.SearchConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'mailings.apps.MailingsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'windstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.menu.menu'
            ],
            'libraries':{
                'custom_filters': 'core.templatetags.custom_filters',
                'subscribe_form_tag': 'core.templatetags.subscribe_form_tag',
            }
        },
    },
]

WSGI_APPLICATION = 'windstore.wsgi.application'


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE"),
        "NAME": os.environ.get("DATABASE_DATABASE"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": os.environ.get("DATABASE_PORT"),
        "OPTIONS": {
            "options": "-c search_path=wstore",
        }
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_URL = 'static/'


MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'profile'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'

CART_SESSION_ID = 'cart'

load_dotenv(find_dotenv())
UNISENDER_API_KEY = os.getenv('UNISENDER_API_KEY')
UNISENDER_COMMON_LIST_ID = '2'
