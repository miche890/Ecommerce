"""
Django settings for Ecommerce project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
import environ

import cloudinary
import cloudinary.uploader
import cloudinary.api

from django.core.management.utils import get_random_secret_key
import dj_database_url
from pathlib import Path
import django.contrib.staticfiles

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY', default=get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'ecommerce-app.fly.dev']  # <-- Updated!

CSRF_TRUSTED_ORIGINS = ['https://ecommerce-app.fly.dev']  # <-- Updated!

CORS_ALLOW_ALL_ORIGINS = True

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'corsheaders',
    'cloudinary',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'apps.authentication',
    'apps.cliente',
    'apps.inventario',
    "apps.cart",
    "apps.marketing"
]

cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME', default='danzjuq3j'),
    api_key=os.environ.get('CLOUDINARY_API_KEY', default='396452838242911'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET', default='llk-KC-UcrOtkxTi7u_qGBZjc6Q'),
    secure=True,
)

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.common.CommonMiddleware',
]

# Cookies

SESSION_COOKIE_NAME = 'sessionid'  # use the sessionid in your views code
# the module to store sessions data
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# age of cookie in seconds (default: 2 weeks)
SESSION_COOKIE_AGE = 24 * 60 * 60 * 7  # the number of seconds for only 7 for example
# whether a user's session cookie expires when the web browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# whether the session cookie should be secure (https:// only)
SESSION_COOKIE_SECURE = False

ROOT_URLCONF = 'Ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR) + '/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.cart.context_processor.total_cart',
                'apps.cart.context_processor.products_cart',
                'apps.marketing.context_processor.get_promociones',
                'apps.inventario.context_processor.get_categorias'
            ],
        },
    },
]

WSGI_APPLICATION = 'Ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': env.db(default='sqlite://db.sqlite3')  # <-- Updated!
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# if not DEBUG:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# else:
#     STATICFILES_DIRS = [
#         BASE_DIR / 'static',
#     ]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# print(BASE_DIR)
# print(STATIC_ROOT)


MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jazzmin settings
JAZZMIN_SETTINGS = {
    'site_title': 'Medtgol',
    'site_header': 'Medtgol',
    'site_brand': 'Medtgol',
    'site_logo': 'img/logos/logo-removebg-preview.png',
    'login_logo': 'img/logos/logo-removebg-preview.png',
    'login_logo_dark': None,
    'site_logo_classes': 'brand-image-xl',
    'site_icon': None,
    'welcome_sign': 'Bienvenido al Sitio Administrativo',
    'copyright': 'Medtgol Admin',
    # 'search_model': ['auth.User', 'auth.Group'],
    'user_avatar': None,
    # TOP MENU
    # 'topmenu_links': [
    #     {'name': 'Panel', 'url': 'admin:index', 'permissions': ['auth.view_user']},
    #     {'model': 'auth.User'},
    #     {'model': 'cliente.Cliente'},
    #     {'model': 'cliente.Proveedor'},
    #     {'model': 'inventario.Producto'},
    #     {'model': 'inventario.Inventario'},
    # ],
    # USER MENU
    'usermenu_links': [],
    # SIDE MENU
    'show_sidebar': True,
    'navigation_expanded': True,
    'hide_apps': [],
    'hide_models': [],
    # 'order_with_respect_to': ['auth', 'projects', 'projects.Project'],
    'icons': {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "cliente.Cliente": "fas fa-address-book",
        "cliente.Proveedor": "fas fa-warehouse",
        "inventario.Categoria": "fas fa-tags",
        "inventario.Producto": "fas fa-shapes",
        "inventario.Inventario": "fas fa-boxes",
        "inventario.OrdenCompra": "fas fa-receipt",
        "inventario.CompraProducto": "fas fa-shopping-cart",
        "marketing.Banners": "fas fa-image",
        "marketing.VideosPromocionales": "fas fa-video",
        'authtoken.TokenProxy': 'fas fa-key'
    },
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',
    # RELATED MODAL
    'related_modal_active': False,
    # UI TWEAKS
    'custom_css': 'css/jazzmin.css',
    'custom_js': None,
    'use_google_fonts_cdn': True,
    'show_ui_builder': False,
    # CHANGE VIEW
    'changeform_format': 'horizontal_tabs',
    'changeform_format_overrides': {'auth.user': 'collapsible', 'auth.group': ' vertical_tabs'},
    'language_chooser': False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logfile.log',  # Ruta al archivo de logs
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
