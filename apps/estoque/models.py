from django.db import models


class Produto(models.Model):
    nome = models.CharField("Nome", max_length=255)
    descricao = models.TextField("Descrição", blank=True)
    quantidade = models.IntegerField("Quantidade em estoque", default=0)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class Movimentacao(models.Model):
    TIPO_CHOICES = (
        ("ENTRADA", "Entrada"),
        ("SAIDA", "Saída"),
    )

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="movimentacoes", verbose_name="Produto")
    tipo = models.CharField("Tipo", max_length=10, choices=TIPO_CHOICES)
    quantidade = models.PositiveIntegerField("Quantidade")
    data = models.DateTimeField("Data", auto_now_add=True)
    observacao = models.TextField("Observação", blank=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.produto.nome} ({self.quantidade})"

    def save(self, *args, **kwargs):
        # Ajusta a quantidade do produto apenas na criação
        if not self.pk:
            if self.tipo == "ENTRADA":
                self.produto.quantidade += self.quantidade
            else:
                self.produto.quantidade -= self.quantidade
            self.produto.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"
