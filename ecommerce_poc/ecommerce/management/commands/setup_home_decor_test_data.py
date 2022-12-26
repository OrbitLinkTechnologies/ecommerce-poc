from django.db import transaction
from django.core.management.base import BaseCommand

from ecommerce.models import HomeDecor
from ecommerce.management.commands.factories import (
    HomeDecorFactory
)

home_decor = HomeDecorFactory()
home_decor.product_name
home_decor.product_category
home_decor.product_manufacturer
home_decor.product_brand
home_decor.product_SKU
home_decor.product_condition
home_decor.product_quantity
home_decor.product_photos
home_decor.home_decor_classification_type

object_count = 5

class Command(BaseCommand):
    help = "Generates Home Decor test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [HomeDecor]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the game consoles
        home_decor_list = []
        for _ in range(object_count):
            home_decor = HomeDecorFactory()
            home_decor_list.append(home_decor)