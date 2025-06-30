from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Documento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='documentos')
    arquivo = models.FileField(upload_to='documentos/')
    nome = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} ({self.cliente.nome})"
