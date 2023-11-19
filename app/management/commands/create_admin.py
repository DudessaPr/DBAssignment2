from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from app.models import User  # Replace 'myapp' with your app name

class Command(BaseCommand):
    help = 'Create a new user with a hashed password'

    def handle(self, *args, **options):
        username = 'ari'
        raw_password = 'ari23'
        role = 'ADMIN'

        # Hash the password securely
        hashed_password = make_password(raw_password)

        # Create a new user profile with the hashed password
        User.objects.create(username=username, password=hashed_password, role = role)

        self.stdout.write(self.style.SUCCESS(f'Successfully created user: {username}'))
