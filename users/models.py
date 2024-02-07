from django.db import models

# Create your models here.
class User(models.Model):
    name =  models.CharField(max_length = 225, verbose_name = 'Имя')
    email = models.EmailField(verbose_name = 'Почта')
    age = models.IntegerField(verbose_name = 'Возраст')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self) -> str:
        return self.title