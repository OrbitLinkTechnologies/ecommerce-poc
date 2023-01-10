# setup_test_data.py

from django.db import transaction
from django.core.management.base import BaseCommand

from ecommerce.models import Generator
from ecommerce.management.commands.factories import (
    GeneratorFactory
)

product = GeneratorFactory()
product.product_name
product.product_category
product.product_manufacturer
product.product_brand
product.product_SKU
product.product_condition
product.product_quantity
product.product_photos
product.generator_classification_type
product.generator_fuel_type
product.generator_continuous_wattage_value

object_count = 100

class Command(BaseCommand):
    help = "Generates generator test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Generator]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the generators
        generators = []
        for _ in range(object_count):
            generator = GeneratorFactory()
            generators.append(generator)