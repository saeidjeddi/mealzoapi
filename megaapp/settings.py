from pathlib import Path
from datetime import timedelta


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-nuzd_n&+g_@uk$t$#t(26=uf-27b14a2nl+015q(hun%cgt$#v"

DEBUG = True
CSRF_TRUSTED_ORIGINS = ["https://takeawaytracker.mealzo.co.uk", "https://marketing.mealzo.co.uk"]

ALLOWED_HOSTS = ['https://takeawaytracker.mealzo.co.uk','datamap.mealzo.co.uk',"*","http://localhost:5173","https://marketing.mealzo.co.uk/","marketing.mealzo.co.uk"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5173",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "https://takeawaytacker.mealzo.co.uk",
    "https://datamap.mealzo.co.uk",
    "http://92.205.131.154",
    "http://localhost:3000",
    "http://92.205.191.109",
    "https://marketing.mealzo.co.uk",

]


CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]

CORS_ALLOW_HEADERS = [ "accept", "referer", "accept-encoding", "authorization", "content-type", "dnt", "origin", "user-agent", "x-csrftoken", "x-sessionid", "x-requested-with"]
CORS_ALLOW_CREDENTIALS = True

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'googleapi.apps.GoogleapiConfig',
    'zohoapi.apps.ZohoapiConfig',
    'exTokenApp.apps.ExtokenappConfig',
    'companies.menulist.apps.MenulistConfig',
    'companies.scoffable.apps.ScoffableConfig',
    'companies.places.apps.CityConfig',
    'companies.foodhub.apps.FoodhubConfig',
    'companies.ubereats.apps.UbereatsConfig',
    'companies.whatthefork.apps.WhattheforkConfig',
    'companies.justeat.apps.JusteatConfig',
    'companies.deliveroo.apps.DeliverooConfig',
    'companies.straightfrom.apps.StraightfromConfig',
    'companies.foodhuse.apps.FoodhuseConfig',
    'companies.cuisine.apps.CuisineConfig',
    'companies.kuick.apps.KuickConfig',
    'companies.postcodes.apps.PostcodesConfig',
    'companies.orderyoyo.apps.OrderyoyoConfig',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'rest_framework',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.url_404.JsonResponse404Middleware',
    # 'middleware.middleware_log.UserAccessLogMiddleware',
    #'megaapp.middleware.cors_middleware.CORSMiddleware',
    #'megaapp.middleware.ip_port_middleware.IPPortAllowMiddleware'
]

ROOT_URLCONF = 'megaapp.urls'

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

WSGI_APPLICATION = 'megaapp.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': "cidbackenddatabase",
#         'USER': "django_user",
#         'PASSWORD': "Radbhn13$%",
#         # 'HOST': "localhost",
#         'HOST': "92.205.57.43",
#         'PORT': '3306',
#         'OPTIONS': {
#             'charset': 'utf8'
#         },
#     },
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
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

TIME_ZONE = 'GMT'

USE_I18N = True

USE_TZ = True



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = 'static/'
# STATICFILES_DIRS = [ BASE_DIR / 'assets' ]
STATIC_ROOT = BASE_DIR / 'static'
# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'accounts.throttles.CustomUserRateThrottle',
    #
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #
    #     'user': '3/day'
    # },



    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#     }
# }

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=24),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',)
}


SPECTACULAR_SETTINGS = {
    'TITLE': 'Mealzo API Panel R&D',
    'DESCRIPTION': 'R&D Team Web API',
    'VERSION': '0.1.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

#--------------------------------------------------
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_AGE = 86400


#----------------------------------------------

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': 'user_access.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#     },
# }


AUTH_USER_MODEL = "accounts.User"

