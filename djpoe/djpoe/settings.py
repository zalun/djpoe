"""Django settings for djpoe project."""

from pathlib import Path

import environ

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
    # django-allauth social account settings
    SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT=(bool, True),
    SOCIALACCOUNT_ONLY=(bool, False),
    GOOGLE_AUTH_CLIENT_ID=(str, ""),
    GOOGLE_AUTH_CLIENT_SECRET=(str, ""),
    WAGTAIL_SITE_NAME=(str, "DJPoe"),
    WAGTAILADMIN_BASE_URL=(str, "http://localhost:8001"),
    WAGTAILADMIN_NOTIFICATION_USE_HTML=(bool, True),
    DEFAULT_FROM_EMAIL=(str, "email@example.com"),
)

env.read_env()

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
]
# Application definition
INSTALLED_APPS = [
    "home",
    # Wagtail
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    # Wagtail 3rd party apps
    "taggit",
    "modelcluster",
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    # django-allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    # debug
    "debug_toolbar",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # django-allauth
    "allauth.account.middleware.AccountMiddleware",
    # Wagtail
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    # debug
    "debug_toolbar.middleware.DebugToolbarMiddleware",
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
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = (BASE_DIR / "static",)
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

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

# django-allauth social account settings

# Should the existing account be automatically recognized as social account
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = env("SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT")
# Should regular accounts login be allowed.
SOCIALACCOUNT_ONLY = env("SOCIALACCOUNT_ONLY")
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": env("GOOGLE_AUTH_CLIENT_ID"),
            "secret": env("GOOGLE_AUTH_CLIENT_SECRET"),
        },
        "scope": ["profile", "email"],
        # Authenticate with google even if account exists without connection to social account
        "EMAIL_AUTHENTICATION": True,
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,
        "FETCH_USERINFO": True,
    }
}


# WAGTAIL SETTINGS

# This is the human-readable name of your Wagtail install
# which welcomes users upon login to the Wagtail admin.
WAGTAIL_SITE_NAME = env("WAGTAIL_SITE_NAME")
# This should be the base URL used to access the Wagtail admin site.
WAGTAILADMIN_BASE_URL = env("WAGTAILADMIN_BASE_URL")
# Replace the search backend
# WAGTAILSEARCH_BACKENDS = {
#  'default': {
#    'BACKEND': 'wagtail.search.backends.elasticsearch8',
#    'INDEX': 'myapp'
#  }
# }

# Wagtail email notifications uses DEFAULT_FROM_EMAIL
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

# Wagtail email notification format
WAGTAILADMIN_NOTIFICATION_USE_HTML = env("WAGTAILADMIN_NOTIFICATION_USE_HTML")

# Allowed file extensions for documents in the document library.
# This can be omitted to allow all files, but note that this may present a security risk
# if untrusted users are allowed to upload files -
# see https://docs.wagtail.org/en/stable/advanced_topics/deploying.html#user-uploaded-files
WAGTAILDOCS_EXTENSIONS = ["csv", "docx", "key", "odt", "pdf", "pptx", "rtf", "txt", "xlsx", "zip"]

# Reverse the default case-sensitive handling of tags
TAGGIT_CASE_INSENSITIVE = True

WAGTAILADMIN_LOGIN_URL = "/accounts/login/"
