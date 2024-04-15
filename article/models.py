from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models
from django.urls import reverse

from authorization.models import User


class Article(models.Model):
    AUDITOR_CHOICES = (
        ('public', 'Публичный'),
        ('privat', 'Приватный')
    )

    title = tinymce_models.HTMLField(verbose_name = 'Заголовок', max_length=30)
    description = models.TextField(verbose_name = 'Описание', max_length=1000, null=True, blank=True)
    content = models.ImageField(verbose_name='Контент', null=True, blank=True)
    tag = models.ForeignKey('Tag', verbose_name='Тег', blank=True, null=True, on_delete=models.PROTECT)
    commnet = models.ForeignKey('Comment', verbose_name='Комментарий', on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, verbose_name= 'Автор', blank=True, null=True, on_delete=models.CASCADE)
    type_content = models.CharField(verbose_name = 'Аудитория', choices = AUDITOR_CHOICES, 
                                    default = 'public', max_length = 200)
    created_at = models.DateTimeField(verbose_name = 'Дата и время', default = timezone.now)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('articles_url', kwargs={'slug': self.slug})
    


class Tag(models.Model):
    tag_name = tinymce_models.HTMLField(verbose_name = 'Тег', max_length= 225)
    # reply = 


    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    def __str__(self):
        return self.tag_name



class Comment(models.Model):
    post = models.ForeignKey(Article, verbose_name='Пост', related_name='post', on_delete=models.CASCADE, null=True, blank=True)
    body = tinymce_models.HTMLField(verbose_name='Тело', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата и время', default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", 
        related_name="author", null=True, blank=True)


    class Meta():
        verbose_name = 'Комент'
        verbose_name_plural = 'Коменнтарии'

    def __repr__(self):
        return self.id


class Group_up(models.Model):
    name_group = tinymce_models.HTMLField(verbose_name = 'Название Сообщства', max_length = 25)
    description_of_group = tinymce_models.HTMLField(verbose_name = 'Описание группы', max_length = 500)
    members = models.ManyToManyField(User, related_name='groups_joined', verbose_name='Участники', blank=True)
    created_at = models.DateTimeField(verbose_name = 'Дата создания', default = timezone.now)

    class Meta():
        verbose_name = 'Группа'
        verbose_name_plural = 'Группа'
    
    def __str__(self) -> str:
        return self.name_group
