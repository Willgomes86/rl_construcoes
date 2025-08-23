from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.CharField(verbose_name='Tipo', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.CharField(verbose_name='Categoria', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='marca',
            field=models.CharField(verbose_name='Marca', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='modelo',
            field=models.CharField(verbose_name='Modelo', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='sku',
            field=models.CharField(verbose_name='SKU', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='codigo_barras',
            field=models.CharField(verbose_name='Código de barras', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='numero_serie',
            field=models.CharField(verbose_name='Número de série', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='lote',
            field=models.CharField(verbose_name='Lote', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='unidade_medida',
            field=models.CharField(verbose_name='Unidade de medida', max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='dimensoes',
            field=models.CharField(verbose_name='Dimensões', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='tamanho',
            field=models.CharField(verbose_name='Tamanho', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='ip',
            field=models.CharField(verbose_name='Grau de proteção (IP)', max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='peso',
            field=models.DecimalField(verbose_name='Peso (kg)', max_digits=10, decimal_places=2, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='data_fabricacao',
            field=models.DateField(verbose_name='Data de fabricação', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='data_compra',
            field=models.DateField(verbose_name='Data de compra', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='validade_lote',
            field=models.DateField(verbose_name='Validade do lote', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.CharField(verbose_name='Fornecedor', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='nota_fiscal',
            field=models.CharField(verbose_name='Nota fiscal', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='localizacao',
            field=models.CharField(verbose_name='Localização', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='quantidade_inicial',
            field=models.IntegerField(verbose_name='Quantidade inicial', default=0),
        ),
        migrations.AddField(
            model_name='produto',
            name='estoque_minimo',
            field=models.IntegerField(verbose_name='Estoque mínimo', default=0),
        ),
        migrations.AddField(
            model_name='produto',
            name='custo',
            field=models.DecimalField(verbose_name='Custo', max_digits=10, decimal_places=2, default=0, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='preco_venda',
            field=models.DecimalField(verbose_name='Preço de venda', max_digits=10, decimal_places=2, default=0, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='garantia_meses',
            field=models.IntegerField(verbose_name='Garantia (meses)', default=0, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='observacoes',
            field=models.TextField(verbose_name='Observações', blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(verbose_name='Imagem', upload_to='produtos/imagens/', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='manual_pdf',
            field=models.FileField(verbose_name='Manual/Datasheet', upload_to='produtos/manuais/', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='ativo',
            field=models.BooleanField(verbose_name='Ativo', default=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='tensao',
            field=models.DecimalField(verbose_name='Tensão (V)', max_digits=10, decimal_places=2, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='corrente',
            field=models.DecimalField(verbose_name='Corrente (A)', max_digits=10, decimal_places=2, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='potencia',
            field=models.DecimalField(verbose_name='Potência (W)', max_digits=10, decimal_places=2, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='vmp',
            field=models.DecimalField(verbose_name='Vmp (V)', max_digits=10, decimal_places=2, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='imp',
            field=models.DecimalField(verbose_name='Imp (A)', max_digits=10, decimal_places=2, blank=True, null=True),
        ),
    ]
