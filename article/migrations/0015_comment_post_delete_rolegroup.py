# Generated by Django 5.0.1 on 2024-04-02 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_remove_group_up_members_group_group_up_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='article.article'),
        ),
        migrations.DeleteModel(
            name='RoleGroup',
        ),
    ]
