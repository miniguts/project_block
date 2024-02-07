# Generated by Django 5.0.1 on 2024-02-05 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=225, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='type_conten',
            field=models.CharField(choices=[('public', 'Публичный'), ('privat', 'Приватный')], default='public', max_length=200, verbose_name='Аудитория'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.tag', verbose_name='Тег'),
        ),
    ]