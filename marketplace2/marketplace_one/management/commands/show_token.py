from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Displays the authentication token for a specified user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the user whose token you want to see')

    def handle(self, *args, **options):
        username = options['username']
        try:
            user = User.objects.get(username=username)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Token created for user {username}: {token.key}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Token for user {username}: {token.key}"))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"User '{username}' not found"))
