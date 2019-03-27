from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os


class Banner(models.Model):
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    titulo = models.CharField(max_length=255, null=True, blank=True)
    subtitulo = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)
    is_blank = models.BooleanField(default=False, verbose_name='Abrir em uma nova página')
    imagem = ProcessedImageField(
        upload_to='banners/%Y/%m/%d',
        processors=[ResizeToFill(1950, 1000)],
        format='JPEG',
        options={'quality': 60},
    )
    thumbnail_horizontal = ImageSpecField(
        source='imagem',
        processors=[ResizeToFill(300, 80)],
        format='JPEG',
        options={'quality': 60}
    )

    def __str__(self):
        return self.descricao

    # def delete(self, using=None, keep_parents=False):
    #     print('Excluindo imagem')
    #     print('imagem', self.imagem.path)
    #     os.remove(self.file.path)
    #     os.remove(self.imagem.path)
    #     return super().delete(using, keep_parents)


@receiver(pre_delete, sender=Banner)
def handler_pre_delete(sender, instance, **kwargs):
    os.remove(instance.imagem.path)
    print('sender', sender)
