from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ProdutoForm, EntradaProdutoForm, SaidaProdutoForm
from .models import Produto


def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, "estoque/produto_list.html", {"produtos": produtos})


def produto_create(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto cadastrado com sucesso!")
            return redirect("estoque:produto_list")
    else:
        form = ProdutoForm()
    return render(request, "estoque/produto_form.html", {"form": form})


def entrada_create(request):
    if request.method == "POST":
        form = EntradaProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Entrada registrada com sucesso!")
            return redirect("estoque:produto_list")
    else:
        form = EntradaProdutoForm()
    return render(
        request,
        "estoque/movimentacao_form.html",
        {"form": form, "titulo": "Entrada de Produto"},
    )


def saida_create(request):
    if request.method == "POST":
        form = SaidaProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Saída registrada com sucesso!")
            return redirect("estoque:produto_list")
    else:
        form = SaidaProdutoForm()
    return render(
        request,
        "estoque/movimentacao_form.html",
        {"form": form, "titulo": "Saída de Produto"},
    )
