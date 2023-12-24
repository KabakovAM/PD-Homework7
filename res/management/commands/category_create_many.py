from django.core.management.base import BaseCommand
from res.models import Category


class Command(BaseCommand):
    help = 'Create category'

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            category = Category(category_name=f'Category{i}')
            category.save()
            self.stdout.write(f'{category}')
