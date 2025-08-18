from django.urls import path
from . import views

app_name = "estoque"

urlpatterns = [
    path("produtos/", views.produto_list, name="produto_list"),
    path("produtos/novo/", views.produto_create, name="produto_create"),
    path("entrada/", views.entrada_create, name="entrada_create"),
    path("saida/", views.saida_create, name="saida_create"),
]
