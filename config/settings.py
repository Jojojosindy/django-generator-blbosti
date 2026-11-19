"""Nastavení: vývoj na počítači + nasazení na Render."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Render automaticky nastavuje proměnnou RENDER. Lokálně je DEBUG zapnutý.
DEBUG = os.getenv("DEBUG", "0" if os.getenv("RENDER") else "1") == "1"

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    if DEBUG:
        SECRET_KEY = "pouze-pro-lokalni-vyvoj-nikdy-nepouzit-na-hostingu"
    else:
        raise RuntimeError("Na hostingu nastav DJANGO_SECRET_KEY v Environment variables.")

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
render_hostname = os.getenv("RENDER_EXTERNAL_HOSTNAME")
if render_hostname:
    ALLOWED_HOSTS.append(render_hostname)
# Volitelné další domény, např. vlastnidomena.cz,www.vlastnidomena.cz
ALLOWED_HOSTS += [x.strip() for x in os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",") if x.strip()]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "generator",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": []},
    }
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# Žádná databáze není potřeba – server jen náhodně vybírá texty.
LANGUAGE_CODE = "cs"
TIME_ZONE = "Europe/Prague"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
    }
}

# Render má HTTPS před aplikací (proxy). Django pak správně pozná protokol.
if os.getenv("RENDER"):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
