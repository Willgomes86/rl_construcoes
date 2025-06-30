from django.db import models
from django.conf import settings
from datetime import timedelta

TIPOS = [
    ('Pagar', 'Conta a Pagar'),
    ('Receber', 'Conta a Receber'),
]

class Conta(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()
    tipo = models.CharField(max_length=10, choices=TIPOS)
    pago = models.BooleanField(default=False)
    data_lancamento = models.DateTimeField(auto_now_add=True)

    @property
    def data_alerta(self):
        """Retorna a data de alerta considerando dias úteis."""
        feriados = getattr(settings, 'FERIADOS', [])
        data = self.vencimento
        if data.weekday() >= 5 or data in feriados:
            data -= timedelta(days=1)
        return data

    def __str__(self):
        return f"{self.descricao} - {self.tipo}"
