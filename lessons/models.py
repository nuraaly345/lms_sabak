from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    video = models.FileField(upload_to='video/%Y/%m/%d/', verbose_name='Видео', blank=True)
    lecturer = models.CharField(max_length=150, verbose_name='Лектор')
    description = models.CharField(max_length=150, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Загружен')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return self.title

  


    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profie for user {}'.format(self.user.username)