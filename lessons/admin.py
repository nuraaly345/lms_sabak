from django.contrib import admin
from .models import *


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'video', 'category', 'lecturer', 'description', 'created_at', 'is_published',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'lecturer')
    list_editable = ('is_published', 'category')
    list_filter = ('is_published', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Category, CategoryAdmin)
