from __future__ import unicode_literals

SECRET_KEY = "22b9a6ed-1f33-4e75-beb7-23eeb8148e2024fb660e-8a01-47df-8ac0-5edbf5fee02b9f6d1bb2-9cd8-4f94-b23f-c0fb19040c6b"
NEVERCACHE_KEY = "114c6ab3-587d-4e7b-96cb-0db732fb807be3c1438f-5985-42d6-a311-23c66566ada071e0b5eb-537e-429d-becc-afc1d6220cc2"
ALLOWED_HOSTS = ['localhost']

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "mysecretpassword",
        "HOST": "db",
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

CACHE_MIDDLEWARE_SECONDS = 60

CACHE_MIDDLEWARE_KEY_PREFIX = "mezzanine-project"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
