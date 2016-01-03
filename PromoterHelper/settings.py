
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '))io@^zm$(1xlw&8kvrlluz37zmcqjxd9501!86$t=hddv=0o%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_BACKENDS = {}

RAPIDSMS_HANDLERS = (
    'sms.handlers.create_group.CreateHandler',
    # 'sms.handlers.join_group.JoinHandler',
    # 'sms.handlers.msg_group.BroadcastHandler',
)



INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # External apps
    'django_tables2',
    'selectable',
    # RapidSMS
    'rapidsms',
    'rapidsms.contrib.handlers',
    'rapidsms.contrib.messagelog',
    'rtwilio',
    'rest_framework',
    'sms',


)

if DEBUG:
    INSTALLED_APPS += (
        'rapidsms.backends.database',
        'rapidsms.contrib.httptester',
    )

    INSTALLED_BACKENDS['message_tester'] = {
        'ENGINE': 'rapidsms.backends.database.DatabaseBackend',
    }

    RAPIDSMS_HANDLERS += (
        'rapidsms.contrib.echo.handlers.echo.EchoHandler',
        'rapidsms.contrib.echo.handlers.ping.PingHandler',
    )

if all('TWILIO_%s' % name in os.environ for name in ['ACCOUNT_SID', 'AUTH_TOKEN', 'NUMBER']):
    INSTALLED_BACKENDS['twilio-backend'] = {
        'ENGINE': 'rtwilio.outgoing.TwilioBackend',
        'config': {
            'account_sid': os.environ['ACdc71922c48d264681c6ef9e748e01c45'],
            'auth_token': os.environ['ca4cc7d244c0b953fc6d212b74e31b4e'],
            'number': os.environ['+13313056575'],
        }
    }
# TWILIO_ACCOUNT_SID
# TWILIO_AUTH_TOKEN
# TWILIO_NUMBER
# +13313056575
# Account Sid
# ACdc71922c48d264681c6ef9e748e01c45
# Auth Token
# ca4cc7d244c0b953fc6d212b74e31b4e
#0703857289

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'PromoterHelper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['[os.path.join(BASE_DIR, "templates")]'],
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

WSGI_APPLICATION = 'PromoterHelper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)
# TEMPLATE_DIRS = [os.path.join(BASE_DIR, "templates")]
