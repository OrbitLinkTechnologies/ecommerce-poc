# setup_test_data.py

from django.db import transaction
from django.core.management.base import BaseCommand

from ecommerce.models import Generator
from ecommerce.management.commands.factories import (
    GeneratorFactory
)

object_count = 100

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Generator]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the users
        generators = []
        for _ in range(object_count):
            generator = GeneratorFactory()
            generators.append(generator)