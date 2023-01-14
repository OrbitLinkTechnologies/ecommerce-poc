from ecommerce.models import HomeDecor
from django.core.management.base import BaseCommand
from django.db import transaction
import json
from decouple import config as dev_config
from django.conf import settings
import stripe
# NOTE: we are only going to use json config files in the future
# this is how all configuration imports will work

if settings.DEBUG == True:
  pass
else:
  with open('/etc/ecommerce_config.json') as config_file:
    config = json.load(config_file)

if settings.DEBUG == True:
  stripe.api_key = dev_config("STRIPE_SECRET_KEY")
else:
  stripe.api_key = config["STRIPE_SECRET_KEY"]

class Command(BaseCommand):

  help = "Generates Home Decor Stripe Products for Test Data"

  @transaction.atomic
  def handle(self, *args, **kwargs):
    self.stdout.write("Generating Home Decor Stripe Products")
    home_decor_objects = HomeDecor.objects.all()
    for home_decor in home_decor_objects:
      response = stripe.Product.create(name = home_decor.product_name)
      home_decor.stripe_product_id = response.id
      home_decor.save()