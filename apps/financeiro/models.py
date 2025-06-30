from django.db import models

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

    def __str__(self):
        return f"{self.descricao} - {self.tipo}"
