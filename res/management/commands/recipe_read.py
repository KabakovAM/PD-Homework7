from django.core.management.base import BaseCommand
from Ex007.models import Good

class Command(BaseCommand):
    help = 'Read good by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Good ID')

    def handle (self, *args, **kwargs):
        pk = kwargs.get('pk')
        good = Good.objects.filter(pk=pk).filter()
        self.stdout.write(f'{good}')