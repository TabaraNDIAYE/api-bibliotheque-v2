# bibliotheque_project/settings.py
import os
from pathlib import Path
from datetime import timedelta
import dj_database_url
from dotenv import load_dotenv

# Charger .env en développement local
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-dev-key-change-me')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',  # Accepte tous les sous-domaines Render
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
]

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Packages tiers
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'corsheaders',
    # Notre application
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← AJOUTER ICI
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bibliotheque_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bibliotheque_project.wsgi.application'

# Base de données - PostgreSQL via DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuration WhiteNoise
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS
CORS_ALLOW_ALL_ORIGINS = True

# DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

# JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}
# Configuration Jazzmin - Thème moderne pour l'admin
JAZZMIN_SETTINGS = {
    # Titre de la fenêtre
    "site_title": "Bibliothèque API Admin",
    
    # Titre dans la barre de navigation
    "site_header": "Bibliothèque API",
    
    # Titre sur la page d'accueil
    "site_brand": "Bibliothèque API Admin",
    
    # Logo (optionnel - mettez votre image dans static/)
    # "site_logo": "img/logo.png",
    
    # Icône du logo
    # "site_logo_classes": "img-circle",
    
    # Texte de bienvenue
    "welcome_sign": "Bienvenue sur l'administration de la Bibliothèque API",
    
    # Copyright
    "copyright": "Bibliothèque API - TP Django REST",
    
    # Icône de recherche
    "search_model": "auth.User",
    
    # Champs à afficher dans l'index
    "show_ui_builder": True,
    
    # Thème (par défaut)
    "theme": "darkly",  # Options: default, darkly, flatly, cosmo, journal, lumen, sandstone, solar, superhero, united, yeti
    
    # Couleur principale (si thème personnalisé)
    "primary_color": "#0d6efd",  # Bleu
    
    # Navigation latérale
    "navigation_expanded": True,
    
    # Icônes des modèles (FontAwesome)
    "icons": {
        "auth.User": "fas fa-users",
        "auth.Group": "fas fa-users-cog",
        "api.Auteur": "fas fa-user-edit",
        "api.Livre": "fas fa-book",
        "api.Tag": "fas fa-tags",
        "api.Emprunt": "fas fa-hand-holding-heart",
        "api.ProfilLecteur": "fas fa-id-card",
    },
    
    # Personnalisation des onglets
    "custom_links": {
        "api": [{
            "name": "Voir l'API",
            "url": "/api/",
            "icon": "fas fa-globe",
            "new_window": True
        }]
    },
}

# Configuration Jazzmin
JAZZMIN_SETTINGS = {
    "site_title": "Bibliothèque API",
    "site_header": "Bibliothèque API",
    "site_brand": "Bibliothèque",
    "welcome_sign": "Bienvenue sur l'administration",
    "copyright": "Bibliothèque API - TP Django REST",
    "theme": "darkly",  # Thème sombre moderne
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
    "dark_mode_theme": "darkly",
}