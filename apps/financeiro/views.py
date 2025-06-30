from django.shortcuts import render, redirect
from .models import Conta
from datetime import datetime, timedelta

def listar_contas(request):
    contas = Conta.objects.all().order_by('vencimento')
    return render(request, 'financeiro/listar.html', {'contas': contas})

def cadastrar_conta(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        vencimento = request.POST.get('vencimento')
        tipo = request.POST.get('tipo')
        Conta.objects.create(descricao=descricao, valor=valor, vencimento=vencimento, tipo=tipo)
        return redirect('listar_contas')
    return render(request, 'financeiro/cadastrar.html')
