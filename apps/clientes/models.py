from django.db import models

class Cliente(models.Model):
    nome = models.CharField("Nome completo", max_length=255)
    cpf_cnpj = models.CharField("CPF ou CNPJ", max_length=20, unique=True)
    email = models.EmailField("E-mail", blank=True)
    telefone = models.CharField("Telefone", max_length=20, blank=True)
    endereco = models.TextField("Endereço", blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class AnexoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='anexos', verbose_name="Cliente")
    arquivo = models.FileField("Arquivo", upload_to='anexos/')
    data_upload = models.DateTimeField("Data do Upload", auto_now_add=True)

    def __str__(self):
        return f"Anexo de {self.cliente.nome}"

    class Meta:
        verbose_name = "Anexo de Cliente"
        verbose_name_plural = "Anexos de Clientes"
