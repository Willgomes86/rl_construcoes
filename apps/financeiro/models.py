from django.db import models
from apps.clientes.models import Cliente

class Conta(models.Model):
    TIPO_CHOICES = (
        ('PAGAR', 'Conta a Pagar'),
        ('RECEBER', 'Conta a Receber'),
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='contas',
        verbose_name="Cliente"
    )
    tipo = models.CharField(
        "Tipo",
        max_length=10,
        choices=TIPO_CHOICES
    )
    descricao = models.CharField("Descrição", max_length=255)
    valor = models.DecimalField("Valor (R$)", max_digits=10, decimal_places=2)
    data_vencimento = models.DateField("Data de Vencimento")
    pago = models.BooleanField("Pago", default=False)
    data_pagamento = models.DateField("Data do Pagamento", null=True, blank=True)
    comprovante = models.FileField("Comprovante", upload_to='comprovantes/', null=True, blank=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.cliente.nome} - R$ {self.valor}"

    class Meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"
        ordering = ['-data_vencimento']
