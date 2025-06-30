from django.core.management.base import BaseCommand
from datetime import date
from apps.financeiro.models import Conta

class Command(BaseCommand):
    help = 'Verifica contas com alerta para o dia atual'

    def handle(self, *args, **options):
        hoje = date.today()
        contas = Conta.objects.all()
        alertas = [c for c in contas if c.data_alerta == hoje]
        if alertas:
            self.stdout.write('Contas com alerta para hoje:')
            for conta in alertas:
                self.stdout.write(f'- {conta.descricao} ({conta.vencimento})')
        else:
            self.stdout.write('Nenhuma conta com alerta para hoje.')
