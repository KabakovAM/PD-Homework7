from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import models


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Имя пользователя')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Новый пароль')
    password2 = forms.CharField(label='Подверждение пароля')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password'].label = 'Пароль'

class NewRecipe(forms.Form):
    recipe_name = forms.CharField(max_length=100, label='Название блюда')
    description = forms.CharField(max_length=500, label='Описание', widget=forms.Textarea)
    products = forms.CharField(label='Продукты', widget=forms.Textarea)
    steps = forms.CharField(label='Рецепт', widget=forms.Textarea)
    time = forms.CharField(max_length=10, label='Время приготовления')
    picture = forms.ImageField(label='Фото блюда')
    category_name = forms.CharField(max_length=100, label='Категория блюда')

class UpdateRecipe(forms.Form):
    recipe_name = forms.CharField(max_length=100, label='Название блюда')
    description = forms.CharField(max_length=500, label='Описание', widget=forms.Textarea)
    products = forms.CharField(label='Продукты', widget=forms.Textarea)
    steps = forms.CharField(label='Рецепт', widget=forms.Textarea)
    time = forms.CharField(max_length=10, label='Время приготовления')
    picture = forms.ImageField(label='Фото блюда')
    category_name = forms.CharField(max_length=100, label='Категория блюда')
