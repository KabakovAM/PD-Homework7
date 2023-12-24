from django.core.management.base import BaseCommand
from res.models import Recipe, Category
import datetime
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create recipe'
  
    def handle (self, *args, **kwargs):
        for i in range(100):
            recipe = Recipe(
            recipe_name = f'Recipe{i}',
            description = f'Description{i}',
            steps = f'Steps{i}',
            time = datetime.time(i+1, i+10, i+10),
            author = User.objects.get(pk=1),
            category_name = Category.objects.get(pk=5),
            )
            recipe.save()
            self.stdout.write(f'{recipe}')