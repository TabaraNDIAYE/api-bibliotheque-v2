# bibliotheque_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

from api.views import create_admin

urlpatterns = [
    # ... vos URLs existantes ...
    path('create-admin/', create_admin, name='create_admin'),
]