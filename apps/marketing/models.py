from django.db import models

from cloudinary.models import CloudinaryField

# Create your models here.


class Banners(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    image = CloudinaryField(resource_type='image', verbose_name='Imagen', default='')

    class Meta:
        db_table = 'Foto Publicitaria'
        verbose_name_plural = 'Fotos Publicitarias'
        verbose_name = 'Foto Publicitaria'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        banners = Banners.objects.all()
        if banners:
            if len(banners) >= 5:
                raise TypeError('No se pueden crear mas de 5 Fotos publicitarias, modifica una existente')

        return super().save(*args, **kwargs)

