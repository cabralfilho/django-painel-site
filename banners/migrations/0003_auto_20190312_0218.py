# Generated by Django 2.1.7 on 2019-03-12 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0002_auto_20190312_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]