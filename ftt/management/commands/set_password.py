from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username')
        parser.add_argument('password')

    def handle(self, *args, **options):
        user = User.objects.get(username=options['username'])
        user.set_password(options['password'])
        user.save()
