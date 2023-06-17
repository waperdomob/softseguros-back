from .base import *
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# SECURITY WARNING: don't run with debug turned on in production!
DATABASES = {
    'default': dj_database_url.config(
        default='mysql://root:@localhost:3306/softseguros',
        conn_max_age=600
    )
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'