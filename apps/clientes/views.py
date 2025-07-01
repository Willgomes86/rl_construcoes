from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente, AnexoCliente

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        arquivos = request.FILES.getlist('arquivos')
        if form.is_valid():
            cliente = form.save()
            for arquivo in arquivos[:10]:
                AnexoCliente.objects.create(cliente=cliente, arquivo=arquivo)
            return redirect('clientes/cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_form.html', {'form': form})
