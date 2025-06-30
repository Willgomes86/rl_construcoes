from django.urls import path
from . import views

app_name = 'financeiro'

urlpatterns = [
    path('', views.listar_contas, name='listar_contas'),
    path('nova/', views.cadastrar_conta, name='cadastrar_conta'),
]
