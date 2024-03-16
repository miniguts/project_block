from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models

from authorization.models import User



class Article(models.Model):
    AUDITOR_CHOICES = (
        ('public', 'Публичный'),
        ('privat', 'Приватный')
    )

    title = models.TextField(verbose_name = 'Заголовок')
    description = tinymce_models.HTMLField(verbose_name = 'Описание', max_length=1000, blank=True, null=True)
    content = models.ImageField(verbose_name='Контент', blank=True)
    # tag = models.ForeignKey(Tag, verbose_name='Тег', blank=True, null=True, on_delete=models.PROTECT)
    type_content = models.CharField(verbose_name = 'Аудитория', choices = AUDITOR_CHOICES, default = 'public', max_length = 200)
    created_at = models.DateTimeField(verbose_name = 'Дата и время', default = timezone.now)
    author = models.ForeignKey(User, verbose_name= 'Автор', blank=True, null=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    tag_name = tinymce_models.HTMLField(verbose_name = 'Тег', max_length= 225)
    # count_use =

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    def __str__(self):
        return self.tag_name

class Comment(models.Model):
    comment = tinymce_models.HTMLField(verbose_name = 'Комент')
    created_at = models.DateTimeField(verbose_name='Дата и время', default = timezone.now)
    # author = models.ForeignKey(User, verbose_name='Автор', default=User.username, null=True, on_delete=models.SET_NULL)
    article = models.ForeignKey(Article, verbose_name='Пост', related_name='comments', on_delete=models.CASCADE, null=True, blank=True)


    class Meta():
        verbose_name = 'Комент'
        verbose_name_plural = 'Коменнтарии'

    def __str__(self):
        return self.comment


# Create your models here.
