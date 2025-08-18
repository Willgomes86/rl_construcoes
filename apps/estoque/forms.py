from django import forms
from .models import Produto, Movimentacao


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao"]


class EntradaProdutoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        exclude = ["tipo", "data"]

    def save(self, commit=True):
        self.instance.tipo = "ENTRADA"
        return super().save(commit)


class SaidaProdutoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        exclude = ["tipo", "data"]

    def save(self, commit=True):
        self.instance.tipo = "SAIDA"
        return super().save(commit)
