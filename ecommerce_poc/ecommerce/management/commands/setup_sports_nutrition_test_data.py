from django.db import transaction
from django.core.management.base import BaseCommand

from ecommerce.models import SportsNutrition
from ecommerce.management.commands.factories import (
    SportsNutritionFactory
)

sports_nutrition = SportsNutritionFactory()
sports_nutrition.product_name
sports_nutrition.product_category
sports_nutrition.product_manufacturer
sports_nutrition.product_brand
sports_nutrition.product_SKU
sports_nutrition.product_condition
sports_nutrition.product_quantity
sports_nutrition.product_photos
sports_nutrition.sports_nutrition_classification_type

object_count = 100

class Command(BaseCommand):
    help = "Generates Sports Nutrition test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [SportsNutrition]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        sports_nutrition_list = []
        for _ in range(object_count):
            sports_nutrition = SportsNutritionFactory()
            sports_nutrition_list.append(sports_nutrition)