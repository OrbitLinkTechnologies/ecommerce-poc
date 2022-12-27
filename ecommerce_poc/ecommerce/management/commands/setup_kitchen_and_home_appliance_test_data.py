from django.db import transaction
from django.core.management.base import BaseCommand

from ecommerce.models import KitchenAndHomeAppliance
from ecommerce.management.commands.factories import (
    KitchenAndHomeApplianceFactory
)

kitchen_and_home_appliance = KitchenAndHomeApplianceFactory()
kitchen_and_home_appliance.product_name
kitchen_and_home_appliance.product_category
kitchen_and_home_appliance.product_manufacturer
kitchen_and_home_appliance.product_brand
kitchen_and_home_appliance.product_SKU
kitchen_and_home_appliance.product_condition
kitchen_and_home_appliance.product_quantity
kitchen_and_home_appliance.product_photos
kitchen_and_home_appliance.kitchen_and_home_appliance_classification_type

object_count = 5

class Command(BaseCommand):
    help = "Generates Kitchen and Home Appliance test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [KitchenAndHomeAppliance]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        kitchen_and_home_appliance_list = []
        for _ in range(object_count):
            kitchen_and_home_appliance = KitchenAndHomeApplianceFactory()
            kitchen_and_home_appliance_list.append(kitchen_and_home_appliance)