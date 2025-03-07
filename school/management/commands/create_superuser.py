from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Create a superuser automatically"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = "@wcsadmin"  # Change this to your preferred username
        email = "wcs@gmail.com"  # Change this
        password = "@Mama051093"  # Change this

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser {username} created successfully!"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists."))
