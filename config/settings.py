# Настройки для джанго проекта
from pathlib import Path
import os
import environ

# текущая дериктория нашего проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# секретный ключ нашего приложения
SECRET_KEY = 'django-insecure-z)s+t7jhx-56!(t2u=+b+%+y=d9via*l57_j2ioa+(%@!z7z6n'

# включен ли у нас режим разработки или нет
DEBUG = True

# для айпишников и доменов тех адресов которые имеют доступ к нашему приложению
ALLOWED_HOSTS = ['*']  # *  для открытия доступа для всех

INSTALLED_APPS = [  # тут можно дописывать приложения которые мы будем регистрировать
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog',
    'blog.apps.BlogConfig',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Папка с общими шаблонами
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

WSGI_APPLICATION = 'config.wsgi.application'


'''Задание 1
Подключите СУБД PostgreSQL для работы в проекте, для этого:

Создайте базу данных в ручном режиме.
Внесите изменения в настройки подключения.'''

# Настройки для базы данных с которой будет работать джанго проект
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='5432'),
    }
}

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

LANGUAGE_CODE = 'en-us'  # различные настройки языка и пр

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'  # важная переменная

STATICFILES_DIRS = [
    os.path.join(BASE_DIR / 'static',),
]
# настройка пути

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

AUTH_USER_MODEL = 'users.User'

# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'Victoria23miha@gmail.com'  # email
EMAIL_HOST_PASSWORD = '*******'  # Пароль
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER