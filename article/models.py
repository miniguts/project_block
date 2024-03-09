from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models

from authorization.models import User

class Article(models.Model):
    AUDITOR_CHOICES = (
        ('public', 'Публичный'),
        ('privat', 'Приватный')
    )

    title = models.TextField(verbose_name = 'Заголовок', blank=True)
    description = tinymce_models.HTMLField(verbose_name = 'Описание', null=True, max_length=1000)
    content = models.ImageField(verbose_name='Контент')
    type_conten = models.CharField(verbose_name = 'Аудитория', choices = AUDITOR_CHOICES, default = 'public', max_length = 200)
    created_at = models.DateTimeField(verbose_name = 'Дата и время', default = timezone.now)
    author = models.ForeignKey(User, verbose_name= 'Автор', blank=True, null=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    comment = tinymce_models.HTMLField(verbose_name = 'Комент')
    article = models.ForeignKey(Article, verbose_name='Пост', related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    

    class Meta():
        verbose_name = 'Комент'
        verbose_name_plural = 'Коменнтарии'

    def __str__(self):
        return self.comment

class Tag(models.Model):
    tag_name = tinymce_models.HTMLField(verbose_name = 'Тег', max_length= 225)
    article = models.ForeignKey(Article, verbose_name='Пост', related_name='tags', on_delete=models.CASCADE, null=True, blank=True)
    # count_use =

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    def __str__(self):
        return self.tag_name

# Create your models here.
