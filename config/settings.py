"""
Django settings for daf project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kg8m+m79-_vbx20&d)y)k+o6u0k&-%2dk6ua-9&$w!8_^l%pnt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

MIDDLEWARE_CLASSES = (
    #must be first
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "django.contrib.auth.context_processors.auth",
    'django.core.context_processors.media',
)


ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "daf",
        'USER': "sult",
        'PASSWORD': "admin",
        'HOST': "localhost",
        'PORT': "",
    },
    'static': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "static",
        'USER': "eve",
        'PASSWORD': "admin",
        'HOST': "localhost",
        'PORT': "",
    },
    'bulk': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "bulk",
        'USER': "eve",
        'PASSWORD': "admin",
        'HOST': "localhost",
        'PORT': "",
    },
}

DATABASE_ROUTERS = ['config.router.Router']


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, "data", "media")
MEDIA_URL = '/data/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "data", "djangostatic")

LOGIN_URL = "/"

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "data", "static"),
)


INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #extra packages
    'froala_editor',
    'pure_pagination',
    'django_extensions',
    #my packages
    'apps.users',
    'apps.apies',
    'apps.characters',
    'apps.corporations',
    'apps.static',
    'apps.blog',
    'apps.admin',
    'apps.bulk',
)


PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 4,
    'MARGIN_PAGES_DISPLAYED': 2,
}


CORP_KEY = 4054629
CORP_ID = 98012663
CORP_VCODE = "6bYDnNhI0oLQegw0lk8YiGjBAM8pSiXoN0oABBIchUSIl3dpcs0YnT6mS2Cs9VPa"

#api = eveapi.EVEAPIConnection()
#auth = api.auth(keyID=4054629,
#vCode="6bYDnNhI0oLQegw0lk8YiGjBAM8pSiXoN0oABBIchUSIl3dpcs0YnT6mS2Cs9VPa")
#auth = api.auth(keyID=4133392,
#vCode="0qbKi4q3CBt8r5CTJlJDoTYdhw27jGxiBKpqCx7x0675Kbs00naX2zkTXT1yOfsx")


#### Basevalues for all sorts ofthings
IMAGE_SIZES = (
    ("Tiny", 32),
    ("Small", 64),
    ("Medium", 128),
    ("Large", 256),
    ("Huge", 512),
    ("Special", 200),
)


#amount of allowed api requests to the evesite per second
EVE_API_REQUESTS = 10
#amount of allowed api requests to the evewho per 30 seconds
# http://evewho.com/faq/
EVE_WHO_REQUESTS = 9
#refresh timer (in hours) for updating the AllianceBulk objects
ALLIANCE_REFRESH = 24
