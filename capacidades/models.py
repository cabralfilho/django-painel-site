from django.db import models


class Capacidade(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True, verbose_name='Descrição')
    icone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.titulo
