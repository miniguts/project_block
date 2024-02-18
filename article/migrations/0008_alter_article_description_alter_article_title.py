# Generated by Django 5.0.1 on 2024-02-16 13:42

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_alter_article_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=tinymce.models.HTMLField(max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.TextField(blank=True, verbose_name='Заголовок'),
        ),
    ]