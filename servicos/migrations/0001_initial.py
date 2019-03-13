# Generated by Django 2.1.7 on 2019-03-13 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('resumo', models.TextField(max_length=150)),
                ('conteudo', models.TextField(blank=True, null=True, verbose_name='Conteúdo')),
                ('imagem', models.ImageField(upload_to='servicos/%Y/%m/%d')),
            ],
        ),
    ]
