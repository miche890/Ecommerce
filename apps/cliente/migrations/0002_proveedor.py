# Generated by Django 5.0.4 on 2024-04-25 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nit', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=120, verbose_name='Nombre')),
                ('email', models.CharField(blank=True, max_length=120, null=True, verbose_name='Correo electronico')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Direccion')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telefono')),
                ('contact_name', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nombre del contacto')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
                'db_table': 'proveedor',
            },
        ),
    ]
