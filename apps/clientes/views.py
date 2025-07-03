from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ClienteForm
from .models import Cliente, AnexoCliente

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})


def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        arquivos = request.FILES.getlist('arquivos')

        if form.is_valid():
            cliente = form.save()
            for arquivo in arquivos[:10]:
                AnexoCliente.objects.create(cliente=cliente, arquivo=arquivo)
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('clientes:cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_form.html', {'form': form})


def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})


def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('clientes:cliente_list')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/cliente_form.html', {'form': form})


def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    messages.success(request, 'Cliente deletado com sucesso!')
    return redirect('clientes:cliente_list')


def adicionar_anexo(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        arquivos = request.FILES.getlist('arquivos')
        for arquivo in arquivos[:10]:
            AnexoCliente.objects.create(cliente=cliente, arquivo=arquivo)

        messages.success(request, 'Anexos adicionados com sucesso!')

    return redirect('clientes:cliente_detail', pk=pk)
