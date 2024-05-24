import os
from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import ValidationError
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

    # def save(self, *args, **kwargs):
    #     banners = Banners.objects.all()
    #     if banners:
    #         if len(banners) >= 5:
    #             raise TypeError('No se pueden crear mas de 5 Fotos publicitarias, modifica una existente')
    #
    #     return super().save(*args, **kwargs)


FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 10  # 10mb


def file_validation(file):
    if not file:
        raise ValidationError('No se ha selecionado un archivo.')

    if isinstance(file, UploadedFile):
        if file.size > FILE_UPLOAD_MAX_MEMORY_SIZE:
            raise ValidationError('El archivo no puede pesar mas de 10MB.')


class VideosPromocionales(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    video = CloudinaryField(resource_type='video', verbose_name='Video', validators=[file_validation])
    active = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        db_table = 'Video Promocional'
        verbose_name_plural = 'Videos Promocionales'
        verbose_name = 'Video Promocional'

    def __str__(self):
        return self.title

    def __unicode__(self):
        try:
            public_id = self.video.public_id
        except AttributeError:
            public_id = ''

        return 'Video <%s:%s>' % (self.title, public_id)
