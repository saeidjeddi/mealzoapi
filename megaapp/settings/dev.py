from .core import *
from datetime import timedelta



INSTALLED_APPS += [

    'accounts.apps.AccountsConfig',
    'api.v1.googleapi.apps.GoogleapiConfig',
    'api.v1.zohoapi.apps.ZohoapiConfig',
    'api.v1.companies.foodhub.apps.FoodhubConfig',
    'api.v1.companies.foodhuse.apps.FoodhuseConfig',
    'api.v1.companies.ubereats.apps.UbereatsConfig',
    'api.v1.companies.whatthefork.apps.WhattheforkConfig',
    'api.v1.companies.justeat.apps.JusteatConfig',

    'rest_framework',
    'rest_framework_simplejwt',

    'corsheaders',


]

# در مدلویر قبل از     'corsheaders.middleware.CorsMiddleware' تعریف شده

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'https://92.205.131.154',
    'http://92.205.131.154',

]

CORS_ORIGIN_ALLOW_ALL = True



STATIC_URL = 'static/'



REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=2),
    'ROTATE_REFRESH_TOKENS': True,  
    'BLACKLIST_AFTER_ROTATION': True,  
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': "@flkjkltrhjknloghr0798HGlortyjh%$krtghiIIIIpp)&887ert455(*YYYY]d1",
    'AUTH_HEADER_TYPES': ('Bearer',)
}



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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.authentication.EmailAuthBackend',
]

