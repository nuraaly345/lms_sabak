from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'cat', 'media']
    fields = ['name', 'cat','media']


admin.site.register(Task,TaskAdmin)
