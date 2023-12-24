from django.core.management.base import BaseCommand
from res.models import Category

class Command(BaseCommand):
    help = 'Read category by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Category ID')

    def handle (self, *args, **kwargs):
        pk = kwargs.get('pk')
        category = Category.objects.filter(pk=pk)
        self.stdout.write(f'{category}')