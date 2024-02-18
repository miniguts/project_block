from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)

# Create your models here.
class User(models.Model):
    user_name = models.TextField(verbose_name='Имя', blank=True)
    email = models.EmailField(verbose_name='Почта', blank=True)
    age = models.IntegerField(verbose_name='Возраст', blank=True)
    password = models.CharField(verbose_name="Пароль", blank=True, max_length=128)
    avatar = models.ImageField(verbose_name="Аватарка", null=True)
    # post = 
    # subscribers = 
    # subscriptions =


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self) -> str:
        return self.user_name
    
# class Commetns(models.Model):
#     created_by = models.ForeignKey(User, verbose_name="Автор", blank=True, on_delete=models.CASCADE, null=True)
#     # likes =
#     # reply =
#     created_at = 
#     article_name = 