# Generated by Django 5.0.4 on 2024-04-25 21:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_compraproducto_ordencompra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto', verbose_name='Producto'),
        ),
    ]
