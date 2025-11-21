"""
Django settings for core project.

Скопируйте этот файл в ваш проект и при необходимости настройте переменные окружения.
"""

from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.environ.get("SECRET_KEY", "replace-me-with-env-secret-key")
DEBUG = os.environ.get("DEBUG", "True").lower() in ("1", "true", "yes")

# В продакшене укажите реальные хосты
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",") if not DEBUG else ["*"]

# Application definition
INSTALLED_APPS = [
    # corsheaders должен быть в начале, чтобы корректно добавлял заголовки
    "corsheaders",

    # сторонние
    "jazzmin",
    "modeltranslation",
    "rest_framework",
    "drf_yasg",
    "ckeditor",

    # django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # ваши приложения
    "app.laiding",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    # CorsMiddleware должен быть как можно выше: до CommonMiddleware и после SessionMiddleware
    "corsheaders.middleware.CorsMiddleware",

    # Если используете LocaleMiddleware — можно оставить после cors
    "django.middleware.locale.LocaleMiddleware",

    # CommonMiddleware оставляем после cors
    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database (по умолчанию sqlite, измените на Postgres при необходимости)
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DB_NAME", BASE_DIR / "db.sqlite3"),
        # для postgres можно добавить: USER, PASSWORD, HOST, PORT через env
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# Internationalization
LANGUAGE_CODE = "ru"
TIME_ZONE = "Asia/Bishkek"
USE_I18N = True
USE_TZ = True

# Static / Media
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Jazzmin (пример)
JAZZMIN_SETTINGS = {
    "site_title": "Мой магазин",
    "site_header": "Панель управления",
    "site_brand": "Админка",
    "welcome_sign": "Добро пожаловать в админку",
    "copyright": "Мой проект © 2025",
}

# --- CORS настройки ---
# ВНИМАНИЕ:
# - Для разработки: можно временно включить CORS_ALLOW_ALL_ORIGINS = True
# - В продакшене явно указывайте CORS_ALLOWED_ORIGINS

# Примеры origins, которые вы используете
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    # ваш локальный IP / хост, с которого фронтенд обращается к бэку:
    "http://172.29.110.154:8000",
    # если фронтенд у вас на том же host, но другом порте:
    "http://172.29.110.154:5173",
]

# Для удобства в dev — можно включать все origin (НЕ ДЛЯ ПРОД)
if DEBUG:
    # если хотите разрешить *всех* во время разработки, раскомментируйте:
    # CORS_ALLOW_ALL_ORIGINS = True
    pass

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# Если нужно — явно разрешить заголовки в preflight ответе
CORS_EXPOSE_HEADERS = [
    "Content-Type",
    "X-CSRFToken",
]

# CSRF trusted origins (если вы используете CSRF + фронт на другом origin)
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:9000",
    "http://localhost:9000",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://172.29.110.154:5173",
]

# DRF (пример — при необходимости настраивайте)
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}

# Model translation
LANGUAGES = (
    ("ru", "Русский"),
    ("en", "English"),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = "ru"
MODELTRANSLATION_LANGUAGES = ("ru", "en")

# APPEND_SLASH: если True — Django будет перенаправлять /path -> /path/
# В вашем случае перенаправление могло вызывать отсутствие CORS заголовков на промежуточном ответе.
APPEND_SLASH = True

# Логи (базовые), при необходимости разворотите
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}
