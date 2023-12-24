from django.shortcuts import render
from . import forms
from . import models
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from random import choices
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


class NewLoginView(LoginView):
    template_name = "login.html"
    authentication_form = forms.UserLoginForm


def five_recipe(request):
    recipes = models.Recipe.objects.all()
    if recipes:
        return render(request, 'res/main.html', {'recipes': choices(recipes, k=5)})
    return render(request, 'res/main.html', {'recipes': recipes})


def one_recipe(request, pk):
    recipe = models.Recipe.objects.get(pk=pk)
    return render(request, 'res/recipe.html', {'recipe': recipe})


def all_recipe(request):
    recipes = models.Recipe.objects.all().order_by('category_name')
    return render(request, 'res/all_recipe.html', {'recipes': recipes})


def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'res/register.html', {'form': form})


def new_recipe(request):
    if request.method == 'POST':
        form = forms.NewRecipe(request.POST, request.FILES)
        if form.is_valid():
            recipe = models.Recipe()
            recipe.recipe_name = form.cleaned_data['recipe_name']
            recipe.description = form.cleaned_data['description']
            recipe.products = form.cleaned_data['products']
            recipe.steps = form.cleaned_data['steps']
            recipe.time = form.cleaned_data['time']
            recipe.picture = form.cleaned_data['picture']
            recipe.author = request.user
            category = models.Category.objects.filter(category_name=form.cleaned_data['category_name']).first()
            if category is not None:
                recipe.category_name = category
            else:
                new_category = models.Category(category_name=form.cleaned_data['category_name'])
                new_category.save()
                recipe.category_name = new_category
            recipe.save()
            return redirect('main')
    else:
        form = forms.NewRecipe()
    return render(request, 'res/new_recipe.html', {'form': form})


def update_recipe(request):
    if request.method == 'POST':
        form = forms.UpdateRecipe(request.POST, request.FILES)
        if form.is_valid():
            recipe_name = form.cleaned_data['recipe_name']
            recipe_check = models.Recipe.objects.filter(recipe_name=recipe_name).first()
            if recipe_check is not None:
                recipe_check.recipe_name = recipe_name
                recipe_check.description = form.cleaned_data['description']
                recipe_check.products = form.cleaned_data['products']
                recipe_check.steps = form.cleaned_data['steps']
                recipe_check.time = form.cleaned_data['time']
                recipe_check.picture = form.cleaned_data['picture']
                recipe_check.author = request.user
                category = models.Category.objects.filter(category_name=form.cleaned_data['category_name']).first()
                if category is not None:
                    recipe_check.category_name = category
                else:
                    new_category = models.Category(category_name=form.cleaned_data['category_name'])
                    new_category.save()
                    recipe_check.category_name = new_category
            recipe_check.save()
            return redirect('main')
    else:
        form = forms.UpdateRecipe()
    return render(request, 'res/update_recipe.html', {'form': form})
