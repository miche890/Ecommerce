# Generated by Django 5.0.4 on 2024-04-26 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_proveedor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Proveedores'},
        ),
    ]
