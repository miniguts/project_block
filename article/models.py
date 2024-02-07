from django.db import models
from django.utils import timezone


class Tag(models.Model):
    tag = models.CharField(verbose_name = 'Тег', max_length= 225)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    def __str__(self):
        return self.title

# Create your models here.
class Article(models.Model):
    COLORS_CHOICES = (
        ('public', 'Публичный'),
        ('privat', 'Приватный')
    )

    #autor_id
    title = models.TextField(verbose_name = 'Заголовок', max_length = '225')
    tag = models.ForeignKey(Tag, verbose_name = 'Тег', blank = True, on_delete = models.CASCADE, null = True)
    type_conten = models.CharField(verbose_name = 'Аудитория', choices = COLORS_CHOICES, default = 'public', max_length = 200)
    content = models.ImageField(verbose_name= 'Контент')
    created_at = models.DateTimeField(verbose_name = 'Дата и время', default = timezone.now)
