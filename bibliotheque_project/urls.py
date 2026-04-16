from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views  # Assurez-vous que vos ViewSets sont bien importés

# --- Configuration du routeur DRF (la partie importante) ---
router = DefaultRouter()
router.register(r'auteurs', views.AuteurViewSet, basename='auteur')
router.register(r'livres', views.LivreViewSet, basename='livre')
# Ajoutez ici d'autres ViewSets si nécessaire (ex: tags, emprunts)
# router.register(r'tags', views.TagViewSet, basename='tag')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ceci va rendre toutes les routes de l'API disponibles sous /api/
    path('api/', include(router.urls)),
    # Vous pouvez aussi ajouter une route simple pour la racine de l'API si vous voulez
    # path('', include(router.urls)), # Optionnel: rend l'API aussi accessible à la racine
]