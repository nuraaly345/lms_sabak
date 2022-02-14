from logging import exception
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView, UpdateView, DeleteView


def homepage(request):
    categories = Category.objects.all()
    
    context = {
        'categories_k': categories,
        'title': 'Башкы бет'

    }
    return render(request, 'base.html', context)


def index(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons_k': lessons,
        'title_k': 'LESSONS LIST'
        
    }
    return render(request, 'lessons/index.html', context)


def get_category(request, category_id):
    lessons = Lesson.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'lessons/category.html',
                  {'lessons_k_gk': lessons, 'categories_k_gk': categories, 'category_k_gk': category})


    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'lessons/addpage.html', {'form': form, 'title': ' Сабак кошуу'})



def addcategory(request):
    if request.method == 'POST':
        cat_form = AddCategoryForm(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            return redirect('/')
    else:
        cat_form = AddCategoryForm()
    return render(request, 'lessons/cat_create.html', {"cat_form": cat_form, "title": "Категория түзүү" })


# Колдонуучуну регистрация кылуу
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'lessons/register_done.html', {'user_form': user_form, 'title': 'Каттоо'})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'lessons/register.html', {'user_form':user_form, 'title': 'Каттоо'})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('homepage')
                else:
                    return HttpResponse(' Error')
            else:
                return HttpResponse('Error')
    else:
        form = LoginForm()
    return render(request, 'lessons/login.html', {'form': form, 'title': 'Кирүү'})


# Профил менен иштөө
def profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile_object = user
        return render(request, 'lessons/profile.html', {'profile': profile_object, 'title': 'Жеке маалыматтар'})
    else:
        return redirect('homepage')


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
    
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        print(user_form.is_valid(), profile_form.is_valid())

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Сиздин профилиңиз ийгиликтүү өзгөрдү')
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'lessons/edit.html', {'user_form': user_form, 'profile_form': profile_form, 'title': 'Маалыматтарды өзгөртүү'})

# Сабак кошуу
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'lessons/addpage.html', {'form': form, 'title': ' Сабак кошуу'})



class NewsDetailView(DeleteView):
    model = Lesson
    template_name = 'lessons/detail_lesson.html'
    context_object_name = 'lesson'



class NewsUpdateView(UpdateView):
    model = Lesson
    template_name = 'lessons/addpage.html'

    #fields = ['title', 'video', 'lecturer', 'description', 'is_published','category']
    form_class = AddPostForm


class NewsDeleteView(DeleteView):
    model = Lesson
    success_url = '/'
    template_name = 'lessons/lesson_delete.html'
