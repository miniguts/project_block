# Generated by Django 5.0.1 on 2024-04-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Суперадмин'), (2, 'Админ'), (3, 'Пользователь')], default=3, verbose_name='Роль'),
        ),
    ]
