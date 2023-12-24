from django.core.management.base import BaseCommand
from res.models import Category

class Command(BaseCommand):
    help = 'Delete category by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Category ID')

    def handle (self, *args, **kwargs):
        pk = kwargs.get('pk')
        category = Category.objects.get(pk=pk)
        if category is not None:
            category.delete()
        self.stdout.write(f'{category}')