from ecommerce.models import KitchenAndHomeAppliance
from django.core.management.base import BaseCommand
from django.db import transaction
import json
from decouple import config as dev_config
from django.conf import settings
import stripe
# NOTE: we are only going to use json config files in the future
# this is how all configuration imports will work

if settings.DEBUG == False:
  pass
else:
  with open('/etc/ecommerce_config.json') as config_file:
    config = json.load(config_file)

if settings.DEBUG == False:
  stripe.api_key = dev_config("STRIPE_SECRET_KEY")
else:
  stripe.api_key = config["STRIPE_SECRET_KEY"]

class Command(BaseCommand):

  help = "Generates Kitchen and Home Appliance Stripe Products for Test Data"

  @transaction.atomic
  def handle(self, *args, **kwargs):
    self.stdout.write("Generating Kitchen and Home Appliance Stripe Products")
    kitchen_and_home_appliances = KitchenAndHomeAppliance.objects.all()
    for kitchen_and_home_appliance in kitchen_and_home_appliances:
      response = stripe.Product.create(name = kitchen_and_home_appliance.product_name)
      kitchen_and_home_appliance.stripe_product_id = response.id
      kitchen_and_home_appliance.save()