from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Membro(models.Model):
    nome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    imagem = ProcessedImageField(
        upload_to='membros/%Y/%m/%d/',
        processors=[ResizeToFill(360, 265)],
        format='JPEG',
        options={'quality': 60}
    )

    def __str__(self):
        return self.nome
