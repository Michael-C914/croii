from .base import*

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        # 'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.mysql'),
        # 'NAME': os.environ.get('SQL_DATABASE', os.path.join(BASE_DIR, 'croii_db')),
        # 'USER': os.environ.get('SQL_USER', 'croii_user'),
        # 'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
        # 'HOST': os.environ.get('SQL_HOST', 'localhost'),
        # 'PORT': os.environ.get('SQL_PORT', '3306'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'croii_db',
        'USER': 'croii_user',
        'PASSWORD': 'password',
        'HOST': '0.0.0.0',
        'PORT': '3306',
    }
}

CORS_ALLOW_ALL_ORIGINS = True
