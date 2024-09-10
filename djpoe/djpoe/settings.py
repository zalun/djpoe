"""Django settings for djpoe project."""

from pathlib import Path

import environ  # type: ignore[import-untyped]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.FileAwareEnv(
    DEBUG=(bool, False),
    DATABASE_URL=(str, "sqlite:///djpoe/db.sqlite3"),
    SECRET_KEY=(str),
    # django-allauth regular account settings
    ACCOUNT_AUTHENTICATION_METHOD=(str, "email"),
    ACCOUNT_EMAIL_REQUIRED=(bool, True),
    ACCOUNT_CONFIRM_EMAIL_ON_GET=(bool, True),
    ACCOUNT_EMAIL_VERIFICATION=(str, "mandatory"),
    ACCOUNT_EMAIL_NOTIFICATIONS=(bool, True),
    ACCOUNT_PRESERVE_USERNAME_CASING=(bool, False),
    LOGIN_REDIRECT_URL=(str, "/accounts/profile/"),
)

env.read_env()

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

ALLOWED_HOSTS: list[str] = ["*"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "allauth",
    "allauth.account",
    "helloworld",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "djpoe.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
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

WSGI_APPLICATION = "djpoe.wsgi.application"

# Parse database connection url strings
# like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    "default": env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = Path(BASE_DIR).joinpath("staticfiles")
STATICFILES_DIRS = (Path(BASE_DIR).joinpath("static"),)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# django-allauth regular account settings
ACCOUNT_AUTHENTICATION_METHOD = env("ACCOUNT_AUTHENTICATION_METHOD")
ACCOUNT_EMAIL_REQUIRED = env("ACCOUNT_EMAIL_REQUIRED")
ACCOUNT_CONFIRM_EMAIL_ON_GET = env("ACCOUNT_CONFIRM_EMAIL_ON_GET")
ACCOUNT_EMAIL_VERIFICATION = env("ACCOUNT_EMAIL_VERIFICATION")
ACCOUNT_EMAIL_NOTIFICATIONS = env("ACCOUNT_EMAIL_NOTIFICATIONS")
ACCOUNT_PRESERVE_USERNAME_CASING = env("ACCOUNT_PRESERVE_USERNAME_CASING")
LOGIN_REDIRECT_URL = env("LOGIN_REDIRECT_URL")

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]
