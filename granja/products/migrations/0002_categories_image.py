# Generated by Django 5.0.6 on 2024-06-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='categories', verbose_name='Foto'),
        ),
    ]
