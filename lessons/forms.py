from unicodedata import category
from django import forms
from .models import *
from django.contrib.auth.models import User

class AddCategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['title', 'description', 'author']


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория тандалган эмес'
    

    class Meta:
        model = Lesson
        fields = ['title', 'video', 'lecturer', 'description', 'is_published','category']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Сыр соз', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Сыр сөздү кайталоо', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('passwords dont match')
        return cd['password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True, 
                widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, 
                widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(
                attrs={'class': 'form-control'}
    ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('photo',)