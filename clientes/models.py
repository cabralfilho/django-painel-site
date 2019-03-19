from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
# from django.db.models.signals import pre_save, post_save
# from django.dispatch import receiver


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    link = models.URLField(max_length=255, null=True, blank=True)
    imagem = ProcessedImageField(
        upload_to='clientes/%Y/%m/%d/',
        processors=[ResizeToFit(height=131)],
        format='JPEG',
        options={'quality': 80}
    )

    def __str__(self):
        return self.nome


# Utilizando Signals
# https://docs.djangoproject.com/en/2.1/topics/signals/
# @receiver(pre_save, sender=Cliente)
# def my_handler_pre_save(sender, update_fields, instance, raw, using, *args, **kwargs):
#     print('Pre save cara...')
#     print(sender)
#     print(instance.imagem)
#     instance.nome = instance.nome + 'Testando'
#     print(raw)
#     print(using)
#     print(args)
#     print('update_fields', update_fields)
#     print('----------------')
