from django.shortcuts import render, redirect
from .models import Cliente, Documento
from django.core.files.storage import FileSystemStorage

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar.html', {'clientes': clientes})

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cliente = Cliente.objects.create(nome=nome, email=email, telefone=telefone)

        arquivos = request.FILES.getlist('documentos')
        for arquivo in arquivos[:10]:
            Documento.objects.create(cliente=cliente, arquivo=arquivo, nome=arquivo.name)

        return redirect('listar_clientes')

    return render(request, 'clientes/cadastrar.html')

def visualizar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, 'clientes/visualizar.html', {'cliente': cliente})
