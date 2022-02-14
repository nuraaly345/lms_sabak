from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Аталышы')
    video = models.FileField(upload_to='video/%Y/%m/%d/', verbose_name='Видео', blank=True)
    lecturer = models.CharField(max_length=150, verbose_name='Лектор')
    description = models.CharField(max_length=150, verbose_name='Баяндама')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Загружен')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return self.title

  


    class Meta:
        verbose_name = 'Сабак'
        verbose_name_plural = 'Сабактар'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категориянын аталышы')
    description = models.TextField(verbose_name="Категориянын описаниеси")
    author = models.CharField(max_length=150, verbose_name='Курстун автору')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категориялар'
        ordering = ['title']

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return '{} үчүн профиль'.format(self.user.username)

