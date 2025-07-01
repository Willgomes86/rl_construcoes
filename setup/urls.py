from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),  # mostra o home
    path('clientes/', include('apps.clientes.urls')),
    path('financeiro/', include('apps.financeiro.urls')),
]
