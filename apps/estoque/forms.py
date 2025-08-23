# apps/estoque/forms.py
from django import forms
from .models import Produto, Movimentacao

class DateInput(forms.DateInput):
    input_type = "date"

# ---- Produto ----
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"
        widgets = {
            "data_compra": DateInput(),
            "data_fabricacao": DateInput(),
            "validade_lote": DateInput(),
            "descricao": forms.Textarea(attrs={"rows": 4}),
            "observacoes": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        base = "form-control bg-dark text-light"
        for field in self.fields.values():
            w = field.widget
            if isinstance(w, (forms.TextInput, forms.NumberInput, forms.EmailInput,
                              forms.URLInput, forms.PasswordInput, forms.DateInput,
                              forms.TimeInput, forms.Textarea, forms.Select,
                              forms.SelectMultiple, forms.FileInput)):
                w.attrs.setdefault("class", base)
            elif isinstance(w, forms.CheckboxInput):
                w.attrs.setdefault("class", "form-check-input")

        placeholders = {
            "nome": "Ex.: Módulo Fotovoltaico 550W",
            "unidade_medida": "Ex.: un, m, kg…",
            "localizacao": "Ex.: Almox A • Prat. 03 • Gaveta Cabos 6mm",
            "ip": "Ex.: IP65",
            "dimensoes": "Ex.: 2279 x 1134 x 35 mm",
            "nota_fiscal": "Nº/Chave NF",
        }
        for k, v in placeholders.items():
            if k in self.fields:
                self.fields[k].widget.attrs.setdefault("placeholder", v)

        for k in ["quantidade", "quantidade_inicial", "estoque_minimo",
                  "peso", "custo", "preco_venda", "garantia_meses"]:
            if k in self.fields:
                self.fields[k].widget.attrs.setdefault("min", "0")
        for k in ["custo", "preco_venda", "peso"]:
            if k in self.fields:
                self.fields[k].widget.attrs.setdefault("step", "0.01")

# ---- Movimentações ----
class _BaseMovForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        base = "form-control bg-dark text-light"
        for field in self.fields.values():
            w = field.widget
            if isinstance(w, forms.CheckboxInput):
                w.attrs.setdefault("class", "form-check-input")
            else:
                w.attrs.setdefault("class", base)

class EntradaProdutoForm(_BaseMovForm):
    class Meta:
        model = Movimentacao
        fields = ["produto", "quantidade", "observacao"]

    def save(self, commit=True):
        inst = super().save(commit=False)
        inst.tipo = "ENTRADA"
        if commit:
            inst.save()
        return inst

class SaidaProdutoForm(_BaseMovForm):
    class Meta:
        model = Movimentacao
        fields = ["produto", "quantidade", "observacao"]

    def save(self, commit=True):
        inst = super().save(commit=False)
        inst.tipo = "SAIDA"
        if commit:
            inst.save()
        return inst
