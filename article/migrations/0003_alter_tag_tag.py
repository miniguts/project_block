# Generated by Django 5.0.1 on 2024-02-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_tag_article_type_conten_article_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.TextField(max_length=225, verbose_name='Тег'),
        ),
    ]
