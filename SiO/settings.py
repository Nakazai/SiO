import os
from unipath import Path

# TODO: Muligens må ta med andre PATHs her for at prosjekte ska funke
# BASE_DIR1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
#
# BASE_DIR = Path(__file__).parent
PROJECT_DIR = Path(__file__).parent
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '55ib3m14rm=g(aqcp_k63gcuzp_$hq^@9tc6v_))h0f%u0&c^5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['67.207.72.58', 'www.sioforeninger.no', 'sioforeninger.no']

# TEST_RUNNER = 'django_behave.runner.DjangoBehaveTestSuiteRunner'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Application definition
# TODO: For vær ny app som blir laget må det dannes PATH her
INSTALLED_APPS = [
    # 'django.contrib.member',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    'bootstrap3',
    'coverage',
    'datetimewidget',
    'dedal',
    # 'bootstrapform',
    # 'behave',
    'behave_django',
    'session_security',
    'django_popup_view_field',
    # 'highcharts',
    'crispy_forms',

    'SiO.member',
    'SiO.CoAdmin',
    'SiO.chart',
    'SiO.core',
    # 'SiO.member',
    'SiO.calapp',
    'SiO.post',
    # email 
    'anymail',

]


# TODO: Dette må til slik at db-table får navnet Administrator
AUTH_USER_MODEL = 'CoAdmin.Administrator'

# AUTHENTICATION_BACKENDS = ['SiO.core.views.EmailBackend']


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

# MIDDLEWARE_CLASSES = [

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',

]

ROOT_URLCONF = 'SiO.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_DIR.child('templates')
        ],
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

WSGI_APPLICATION = 'SiO.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# TODO: Kommunikasjon med databasen

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_test',
        'USER': 'postgres',
        'PASSWORD': 'illievski',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/
# TODO: change format of date, but it will change the language as well
LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'nb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = PROJECT_DIR.parent.child('staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

MEDIA_ROOT = PROJECT_DIR.parent.child('media')
MEDIA_URL = '/media/'

# TODO: Her velges det ulike PATH for hvor bruker skal dirigeres til
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_URL = '/'

SESSION_SECURITY_EXPIRE_AFTER = 3600
SESSION_SECURITY_WARN_AFTER = 3000
# SESSION_SECURITY_EXPIRE_AFTER = 10
# SESSION_SECURITY_WARN_AFTER = 5
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ALLOWED_SIGNUP_DOMAINS = ['*']

FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 0o644

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": "key-197955abc889708dd670fb2c8b24b586",
    "MAILGUN_SENDER_DOMAIN": 'test.sioforeninger.no',  # your Mailgun domain, if needed
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
DEFAULT_FROM_EMAIL = "TestSite Team <noreply@sioforeninger.no>"  # if you don't already have this in settin
