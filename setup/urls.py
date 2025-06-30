from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('financeiro/', include(('apps.financeiro.urls', 'financeiro'), namespace='financeiro')),
    path('', include(('apps.clientes.urls', 'clientes'), namespace='clientes')),
]
