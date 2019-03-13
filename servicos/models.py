from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Servico(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Título')
    resumo = models.TextField(max_length=150)
    conteudo = models.TextField(null=True, blank=True, verbose_name='Conteúdo')
    imagem = ProcessedImageField(
        upload_to='servicos/%Y/%m/%d',
        processors=[ResizeToFill(270, 190)],
        format='JPEG',
        options={'quality': 60}
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Serviço'
