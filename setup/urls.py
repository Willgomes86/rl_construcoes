from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),  # mostra o home
    path('clientes/', include('apps.clientes.urls')),
    path('financeiro/', include('apps.financeiro.urls')),
    path('estoque/', include('apps.estoque.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)