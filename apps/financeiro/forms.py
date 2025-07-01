from django import forms
from .models import Conta
from apps.clientes.models import Cliente

class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = '__all__'
        widgets = {
            'data_vencimento': forms.DateInput(attrs={'type': 'date'}),
            'data_pagamento': forms.DateInput(attrs={'type': 'date'}),
        }

class RelatorioForm(forms.Form):
    TIPO_CHOICES = (
        ('', 'Todos'),
        ('PAGAR', 'Contas a Pagar'),
        ('RECEBER', 'Contas a Receber'),
    )

    STATUS_CHOICES = (
        ('', 'Todos'),
        ('pago', 'Pagos'),
        ('pendente', 'Pendentes'),
    )

    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=False, label="Cliente")
    tipo = forms.ChoiceField(choices=TIPO_CHOICES, required=False, label="Tipo")
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Status")
    data_inicio = forms.DateField(required=False, label="Data Início", widget=forms.DateInput(attrs={'type': 'date'}))
    data_fim = forms.DateField(required=False, label="Data Fim", widget=forms.DateInput(attrs={'type': 'date'}))
