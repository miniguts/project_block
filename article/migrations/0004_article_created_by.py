# Generated by Django 5.0.1 on 2024-02-12 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_tag_tag'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Автор'),
        ),
    ]
