from .core import *
from datetime import timedelta


INSTALLED_APPS += [


    'accounts.apps.AccountsConfig',
    'api.v1.googleapi.apps.GoogleapiConfig',
    'api.v1.zohoapi.apps.ZohoapiConfig',

    'rest_framework',
    'rest_framework_simplejwt',


]




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
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=1),
    'ROTATE_REFRESH_TOKENS': True,  
    'BLACKLIST_AFTER_ROTATION': True,  
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': "@flkjkltrhjknloghr0798HGlortyjh%$krtghiIIIIpp)&887ert455(*YYYY]d1",
    'AUTH_HEADER_TYPES': ('Bearer',)
}



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'user.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}






AUTH_USER_MODEL = "accounts.User"

