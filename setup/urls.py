from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('financeiro/', include(('apps.financeiro.urls', 'financeiro'), namespace='financeiro')),
    path('clientes/', include(('apps.clientes.urls', 'clientes'), namespace='clientes')),
    path('', include(('apps.core.urls', 'core'), namespace='core')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
