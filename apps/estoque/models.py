from django.db import models


class Produto(models.Model):
    """Cadastro completo de produtos.

    Projetado para atender diversos itens utilizados pela empresa de
    manutenção/instalação elétrica e de painéis solares.
    """

    nome = models.CharField("Nome", max_length=255)
    tipo = models.CharField("Tipo", max_length=100, blank=True)
    categoria = models.CharField("Categoria", max_length=100, blank=True)
    marca = models.CharField("Marca", max_length=100, blank=True)
    modelo = models.CharField("Modelo", max_length=100, blank=True)
    sku = models.CharField("SKU", max_length=100, blank=True)
    codigo_barras = models.CharField("Código de barras", max_length=100, blank=True)
    numero_serie = models.CharField("Número de série", max_length=100, blank=True)
    lote = models.CharField("Lote", max_length=100, blank=True)
    unidade_medida = models.CharField("Unidade de medida", max_length=10, blank=True)
    dimensoes = models.CharField("Dimensões", max_length=100, blank=True)
    tamanho = models.CharField("Tamanho", max_length=100, blank=True)
    ip = models.CharField("Grau de proteção (IP)", max_length=20, blank=True)
    peso = models.DecimalField("Peso (kg)", max_digits=10, decimal_places=2, blank=True, null=True)
    data_fabricacao = models.DateField("Data de fabricação", blank=True, null=True)
    data_compra = models.DateField("Data de compra", blank=True, null=True)
    validade_lote = models.DateField("Validade do lote", blank=True, null=True)
    fornecedor = models.CharField("Fornecedor", max_length=255, blank=True)
    nota_fiscal = models.CharField("Nota fiscal", max_length=100, blank=True)
    localizacao = models.CharField("Localização", max_length=255, blank=True)

    quantidade = models.IntegerField("Quantidade em estoque", default=0)
    quantidade_inicial = models.IntegerField("Quantidade inicial", default=0)
    estoque_minimo = models.IntegerField("Estoque mínimo", default=0)

    custo = models.DecimalField("Custo", max_digits=10, decimal_places=2, default=0, blank=True)
    preco_venda = models.DecimalField("Preço de venda", max_digits=10, decimal_places=2, default=0, blank=True)
    garantia_meses = models.IntegerField("Garantia (meses)", default=0, blank=True)

    descricao = models.TextField("Descrição", blank=True)
    observacoes = models.TextField("Observações", blank=True)
    imagem = models.ImageField("Imagem", upload_to="produtos/imagens/", blank=True, null=True)
    manual_pdf = models.FileField("Manual/Datasheet", upload_to="produtos/manuais/", blank=True, null=True)

    ativo = models.BooleanField("Ativo", default=True)

    tensao = models.DecimalField("Tensão (V)", max_digits=10, decimal_places=2, blank=True, null=True)
    corrente = models.DecimalField("Corrente (A)", max_digits=10, decimal_places=2, blank=True, null=True)
    potencia = models.DecimalField("Potência (W)", max_digits=10, decimal_places=2, blank=True, null=True)
    vmp = models.DecimalField("Vmp (V)", max_digits=10, decimal_places=2, blank=True, null=True)
    imp = models.DecimalField("Imp (A)", max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        # na criação, caso não seja informada a quantidade,
        # utiliza a quantidade inicial cadastrada
        if not self.pk and self.quantidade == 0:
            self.quantidade = self.quantidade_inicial
        super().save(*args, **kwargs)

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
