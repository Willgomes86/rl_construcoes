from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('novo/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('<int:cliente_id>/', views.visualizar_cliente, name='visualizar_cliente'),
]
