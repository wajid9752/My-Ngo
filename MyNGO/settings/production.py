from .base import *



ALLOWED_HOSTS = ['lurnify.in', 'www.lurnify.in', '3.6.237.69']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR , '/home/ubuntu/lurnify_in/lurnify/templates'],
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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lurnify_db',
        'USER': 'lurnify',
        'PASSWORD': 'Aaeny_0097@',
        'HOST': 'localhost',
        'PORT': '3306',
        'TIME_ZONE': 'Asia/Kolkata',
        'OPTIONS':{
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

STATIC_ROOT = '/home/ubuntu/lurnify_in/lurnify/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    # BASE_DIR / "static",
    '/var/www/static/',
]

MEDIA_ROOT = '/home/ubuntu/lurnify_in/lurnify/media/'
MEDIA_URL = '/media/'

