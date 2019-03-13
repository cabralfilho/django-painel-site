from django.db import models
from ckeditor.fields import RichTextField


class Pagina(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Título')
    conteudo = RichTextField(verbose_name='Conteúdo')
    resumo = models.TextField(max_length=170, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
