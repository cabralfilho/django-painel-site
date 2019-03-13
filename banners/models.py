from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill


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
