from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContaPagarForm, ContaReceberForm, RelatorioForm
from .models import Conta
from datetime import date, timedelta
import holidays
from django.db.models import Sum, Case, When, F, Value as V, DecimalField

BR_HOLIDAYS = holidays.Brazil()


def contas_alerta(request):
    hoje = date.today()
    util = hoje.weekday() < 5 and hoje not in BR_HOLIDAYS

    if util:
        contas = Conta.objects.filter(data_vencimento=hoje, pago=False)
    else:
        anterior = hoje - timedelta(days=1)
        while anterior.weekday() >= 5 or anterior in BR_HOLIDAYS:
            anterior -= timedelta(days=1)
        contas = Conta.objects.filter(data_vencimento=anterior, pago=False)

    return render(request, 'financeiro/contas_alerta.html', {'contas': contas})


def contas_pagar_list(request):
    contas = Conta.objects.filter(tipo='PAGAR').order_by('data_vencimento')
    return render(request, 'financeiro/contas_pagar_list.html', {'contas': contas})


def contas_receber_list(request):
    contas = Conta.objects.filter(tipo='RECEBER').order_by('data_vencimento')
    return render(request, 'financeiro/contas_receber_list.html', {'contas': contas})


def conta_pagar_create(request):
    if request.method == 'POST':
        form = ContaPagarForm(request.POST, request.FILES)
        if form.is_valid():
            conta = form.save(commit=False)
            conta.tipo = 'PAGAR'
            conta.save()
            return redirect('financeiro:contas_pagar')
    else:
        form = ContaPagarForm()
    return render(request, 'financeiro/conta_form_pagar.html', {'form': form, 'tipo': 'PAGAR'})


def conta_receber_create(request):
    if request.method == 'POST':
        form = ContaReceberForm(request.POST, request.FILES)
        if form.is_valid():
            conta = form.save(commit=False)
            conta.tipo = 'RECEBER'
            conta.save()
            return redirect('financeiro:contas_receber')
    else:
        form = ContaReceberForm()
    return render(request, 'financeiro/conta_form_receber.html', {'form': form, 'tipo': 'RECEBER'})


def marcar_como_pago(request, pk):
    conta = get_object_or_404(Conta, pk=pk)
    conta.pago = True
    conta.data_pagamento = date.today()
    conta.save()
    if conta.tipo == 'PAGAR':
        return redirect('financeiro:contas_pagar')
    else:
        return redirect('financeiro:contas_receber')


def relatorios(request):
    form = RelatorioForm(request.GET or None)
    contas = Conta.objects.all()

    if form.is_valid():
        cliente = form.cleaned_data.get('cliente')
        tipo = form.cleaned_data.get('tipo')
        status = form.cleaned_data.get('status')
        data_inicio = form.cleaned_data.get('data_inicio')
        data_fim = form.cleaned_data.get('data_fim')

        if cliente:
            contas = contas.filter(cliente=cliente)
        if tipo:
            contas = contas.filter(tipo=tipo)
        if status == 'pago':
            contas = contas.filter(pago=True)
        elif status == 'pendente':
            contas = contas.filter(pago=False)
        if data_inicio:
            contas = contas.filter(data_vencimento__gte=data_inicio)
        if data_fim:
            contas = contas.filter(data_vencimento__lte=data_fim)

    total = contas.aggregate(
        total_valor=Sum(
            Case(
                When(tipo='RECEBER', then=F('valor')),
                When(tipo='PAGAR', then=F('valor') * V(-1)),
                default=V(0),
                output_field=DecimalField()
            )
        ),
        total_pagas=Sum(
            Case(
                When(pago=True, tipo='PAGAR', then=F('valor') * V(-1)),
                When(pago=True, tipo='RECEBER', then=F('valor')),
                default=V(0),
                output_field=DecimalField()
            )
        ),
        total_recebidas=Sum(
            Case(
                When(pago=True, tipo='RECEBER', then=F('valor')),
                default=V(0),
                output_field=DecimalField()
            )
        ),
        total_pendentes=Sum(
            Case(
                When(pago=False, tipo='PAGAR', then=F('valor') * V(-1)),
                When(pago=False, tipo='RECEBER', then=F('valor')),
                default=V(0),
                output_field=DecimalField()
            )
        )
    )

    context = {
        'form': form,
        'contas': contas,
        'total': total
    }
    return render(request, 'financeiro/relatorio.html', context)


def confirmar_pagamento(request):
    if request.method == 'POST':
        conta_id = request.POST.get('conta_id')
        data_pagamento = request.POST.get('data_pagamento')
        comprovante = request.FILES.get('comprovante')

        conta = get_object_or_404(Conta, pk=conta_id)
        conta.pago = True
        conta.data_pagamento = data_pagamento
        conta.comprovante = comprovante
        conta.save()

        if conta.tipo == 'PAGAR':
            return redirect('financeiro:contas_pagar')
        else:
            return redirect('financeiro:contas_receber')

