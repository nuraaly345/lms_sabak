from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect

def addtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TaskForm()

    return render(request, 'task/task.html', {"form": form, "title": "Тапшырма жөнөтүү"})


def list_task(request):
    task_object = Task.objects.all()
    return render(request, 'task/list_task.html', {'task_object': task_object, 'title': 'Тапшырмалардын тизмеси'})
