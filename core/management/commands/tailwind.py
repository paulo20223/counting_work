from django.core.management.base import BaseCommand, CommandError
import os
from subprocess import call


class Command(BaseCommand):
    help = 'tailwind start'

    def handle(self, *args, **options):
        rc = call("npx tailwindcss -i ./assets/css/tailwind.css -o ./assets/css/style.css --watch", shell=True)
