# Generated by Django 5.0.1 on 2024-03-31 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_rolegroup_remove_comment_article_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.IntegerField(default=0),
        ),
    ]
