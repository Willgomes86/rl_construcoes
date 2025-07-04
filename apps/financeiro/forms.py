from django import forms
from .models import Conta
from apps.clientes.models import Cliente


class BaseContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        exclude = ['tipo']
        widgets = {
            'data_vencimento': forms.DateInput(attrs={'type': 'date'}),
            'data_pagamento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        pago = cleaned_data.get('pago')
        data_pagamento = cleaned_data.get('data_pagamento')
        comprovante = cleaned_data.get('comprovante')

        if pago:
            if not data_pagamento:
                self.add_error('data_pagamento', 'Informe a data do pagamento.')
        else:
            cleaned_data['data_pagamento'] = None
            cleaned_data['comprovante'] = None

        return cleaned_data


class ContaPagarForm(BaseContaForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aqui você pode customizar ainda mais se quiser
        self.fields['descricao'].label = 'Descrição da Conta a Pagar'


class ContaReceberForm(BaseContaForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aqui você pode customizar ainda mais se quiser
        self.fields['descricao'].label = 'Descrição da Conta a Receber'


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

    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        required=False,
        label="Cliente"
    )
    tipo = forms.ChoiceField(
        choices=TIPO_CHOICES,
        required=False,
        label="Tipo"
    )
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        required=False,
        label="Status"
    )
    data_inicio = forms.DateField(
        required=False,
        label="Data Início",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    data_fim = forms.DateField(
        required=False,
        label="Data Fim",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
