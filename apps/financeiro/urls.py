from django.urls import path
from . import views

app_name='financeiro'

urlpatterns = [
    path('pagar/', views.contas_pagar_list, name='contas_pagar'),
    path('receber/', views.contas_receber_list, name='contas_receber'),
    path('nova-pagar/', views.conta_pagar_create, name='nova_conta_pagar'),
    path('nova-receber/', views.conta_receber_create, name='nova_conta_receber'),
    path('pagar/<int:pk>/', views.marcar_como_pago, name='marcar_pago'),
    path('alerta/', views.contas_alerta, name='contas_alerta'),
    path('relatorio/', views.relatorios, name='relatorios'),
    path('confirmar-pagamento/', views.confirmar_pagamento, name='confirmar_pagamento'),
    path('conta/<int:pk>/deletar/', views.conta_delete, name='conta_delete'),

]
