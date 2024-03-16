# Generated by Django 5.0.1 on 2024-03-16 10:27

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_rename_type_conten_article_type_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='article.tag', verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=tinymce.models.HTMLField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.TextField(verbose_name='Заголовок'),
        ),
    ]
