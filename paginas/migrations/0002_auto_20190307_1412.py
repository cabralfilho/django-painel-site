# Generated by Django 2.1.7 on 2019-03-07 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagina',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
