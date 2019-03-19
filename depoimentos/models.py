from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Depoimento(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome do cliente')
    depoimento = models.TextField()
    imagem = ProcessedImageField(
        upload_to='depoimentos/%Y/%m/%d/',
        processors=[ResizeToFill(60, 60)],
        format='JPEG',
        options={'quality': 60}
    )

    def __str__(self):
        return self.nome
