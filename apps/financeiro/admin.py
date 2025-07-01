from django.contrib import admin
from .models import Conta

@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'tipo', 'descricao', 'valor', 'data_vencimento', 'pago']
    list_filter = ['tipo', 'pago']
    search_fields = ['cliente__nome', 'descricao']
from django.contrib import admin

# Register your models here.
