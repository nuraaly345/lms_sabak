from django.urls import path
from .views import *

urlpatterns = [
    path("", addtask, name='addtask'),
    path('task_list/', list_task, name='task-list')
]