# Generated by Django 5.0.4 on 2024-05-11 01:28

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0012_categoria_destacada'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='', max_length=255, null=True, verbose_name='Imagen'),
        ),
    ]
