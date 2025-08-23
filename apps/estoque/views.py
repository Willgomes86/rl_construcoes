# apps/estoque/views.py
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from .forms import ProdutoForm, EntradaProdutoForm, SaidaProdutoForm
from .models import Produto, EntradaProduto, SaidaProduto


# -------------------------
# Produtos
# -------------------------
def produto_list(request):
    """
    Lista de produtos com busca, ordenação e paginação.
    GET params:
      - q: termo de busca (nome, descrição, marca, modelo, sku, código de barras)
      - o: campo de ordenação (ex.: nome, -quantidade, preco_venda)
      - page: página
    """
    q = request.GET.get("q", "").strip()
    order = request.GET.get("o", "nome")

    produtos = Produto.objects.all()

    if q:
        produtos = produtos.filter(
            Q(nome__icontains=q)
            | Q(descricao__icontains=q)
            | Q(marca__icontains=q)
            | Q(modelo__icontains=q)
            | Q(sku__icontains=q)
            | Q(codigo_barras__icontains=q)
            | Q(numero_serie__icontains=q)
        )

    # segurança básica de ordenação
    allowed_orders = {
        "nome",
        "-nome",
        "quantidade",
        "-quantidade",
        "preco_venda",
        "-preco_venda",
        "custo",
        "-custo",
        "marca",
        "-marca",
        "categoria",
        "-categoria",
    }
    if order not in allowed_orders:
        order = "nome"

    produtos = produtos.order_by(order)

    paginator = Paginator(produtos, 20)  # 20 por página
    page_obj = paginator.get_page(request.GET.get("page"))

    ctx = {"page_obj": page_obj, "q": q, "o": order}
    return render(request, "estoque/produto_list.html", ctx)


def produto_create(request):
    """
    Cadastro de produto com upload de arquivos (imagem/manual).
    """
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto cadastrado com sucesso!")
            return redirect("estoque:produto_list")
        messages.error(request, "Corrija os campos destacados.")
    else:
        form = ProdutoForm()

    return render(request, "estoque/produto_form.html", {"form": form})


def produto_update(request, pk):
    """
    Edição de produto.
    """
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado com sucesso!")
            return redirect("estoque:produto_list")
        messages.error(request, "Corrija os campos destacados.")
    else:
        form = ProdutoForm(instance=produto)

    return render(request, "estoque/produto_form.html", {"form": form})


def produto_delete(request, pk):
    """
    Exclusão de produto (POST).
    """
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.delete()
        messages.success(request, "Produto excluído com sucesso!")
        return redirect("estoque:produto_list")

    # opcional: página simples de confirmação
    return render(request, "estoque/produto_confirm_delete.html", {"produto": produto})


# -------------------------
# Movimentações de Estoque
# -------------------------
def entrada_create(request):
    """
    Registro de entrada de produto.
    """
    if request.method == "POST":
        form = EntradaProdutoForm(request.POST)
        if form.is_valid():
            entrada = form.save()
            messages.success(
                request,
                f"Entrada registrada com sucesso! (+{entrada.quantidade} {entrada.produto})",
            )
            return redirect("estoque:produto_list")
        messages.error(request, "Corrija os campos destacados.")
    else:
        form = EntradaProdutoForm()

    return render(
        request,
        "estoque/movimentacao_form.html",
        {"form": form, "titulo": "Entrada de Produto"},
    )


def saida_create(request):
    """
    Registro de saída de produto.
    """
    if request.method == "POST":
        form = SaidaProdutoForm(request.POST)
        if form.is_valid():
            saida = form.save()
            messages.success(
                request,
                f"Saída registrada com sucesso! (-{saida.quantidade} {saida.produto})",
            )
            return redirect("estoque:produto_list")
        messages.error(request, "Corrija os campos destacados.")
    else:
        form = SaidaProdutoForm()

    return render(
        request,
        "estoque/movimentacao_form.html",
        {"form": form, "titulo": "Saída de Produto"},
    )
