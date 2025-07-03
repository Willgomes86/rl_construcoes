from django.urls import path
from . import views


app_name = 'clientes'

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('novo/', views.cliente_create, name='cliente_create'),
    path('<int:pk>/', views.cliente_detail, name='cliente_detail'),  # ✅ Adiciona esta
    path('<int:pk>/editar/', views.cliente_edit, name='cliente_edit'),  # ✅ E esta
    path('<int:pk>/deletar/', views.cliente_delete, name='cliente_delete'),  # ✅ E esta
    path('<int:pk>/adicionar-anexo/', views.adicionar_anexo, name='adicionar_anexo'),

]
