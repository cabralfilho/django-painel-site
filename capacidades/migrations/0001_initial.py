# Generated by Django 2.1.7 on 2019-03-13 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capacidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('icone', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
