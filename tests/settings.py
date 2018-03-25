INSTALLED_APPS = (
    'reportmail',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
SECRET_KEY = "secret_key_for_testing"
MIDDLEWARE_CLASSES = []

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]
