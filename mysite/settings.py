from .email_info import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS, EMAIL_HOST_USER, DEFAULT_FROM_EMAIL,EMAIL_BACKEND
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ')300i%9rx)172ha)ua_*@5lu!v@q7a4pmbm(ov$0b1-fnr-+5j'

if 'runserver' in sys.argv:
    DEBUG = True
else:
    DEBUG = False

if DEBUG == False:
    SECURE_HSTS_SECONDS = 3600
    X_FRAME_OPTIONS = 'DENY'
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE= True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
    SECURE_HSTS_PRELOAD = True
    ENVIRONMENT_NAME = "Kroums-Webdesign Production server"
    ENVIRONMENT_COLOR = "#FF2222"
    SECURE_CONTENT_TYPE_NOSNIFF = True
else:
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_SSL_REDIRECT = False
    SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
    SECURE_HSTS_PRELOAD = False
    ENVIRONMENT_NAME = "Kroums-Webdesign Development server"
    ENVIRONMENT_COLOR = "#503fe7"


ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.pythonanywhere.com', 'www.kroums-webdesign.at', '207.154.225.193', 'kroums-webdesign.at']
INSTALLED_APPS = [
    'django.contrib.sites',
    'django_admin_env_notice',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base_app.apps.BaseAppConfig',
    'service_app.apps.ServiceAppConfig',
    'about_app.apps.AboutAppConfig',
    'contact_app.apps.ContactAppConfig',
    'projects_app.apps.ProjectsAppConfig',
    'references_app.apps.ReferencesAppConfig',
    'info_app.apps.InfoAppConfig',
    'django.contrib.sitemaps',
    'smartfields',
    'django_cleanup.apps.CleanupConfig',
    'admin_honeypot',
    'easy_thumbnails',
    'image_cropping',
]

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'base_app.context_processors.global_footer_info',
                'base_app.context_processors.load_master_objekt',
                'django_admin_env_notice.context_processors.from_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

SITE_ID = 1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'de-ch'

TIME_ZONE = 'Europe/Berlin'


USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'
