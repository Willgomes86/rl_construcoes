from django.urls import path
from . import views

app_name = "estoque"

urlpatterns = [
    # Produtos
    path("produtos/", views.produto_list, name="produto_list"),
    path("produtos/novo/", views.produto_create, name="produto_create"),
    path("produtos/<int:pk>/editar/", views.produto_update, name="produto_update"),
    path("produtos/<int:pk>/excluir/", views.produto_delete, name="produto_delete"),

    # Movimentações
    path("entrada/", views.entrada_create, name="entrada_create"),
    path("saida/", views.saida_create, name="saida_create"),
]
