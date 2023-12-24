from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category_name}'



class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    products = models.TextField()
    steps = models.TextField()
    time = models.CharField(max_length=10)
    picture = models.ImageField(default=None, upload_to=settings.MEDIA_ROOT)
    reg_data = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'Recipe: {self.recipe_name}, time: {self.time}, author: {self.author}, category: {self.category_name}'



