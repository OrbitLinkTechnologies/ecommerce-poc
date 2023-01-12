from ecommerce.models import Generator, Price
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

  help = "Generates Stripe Products for Test Data"

  # currently there is no way to delete products that have prices associated with them via the API
  @transaction.atomic
  def handle(self, *args, **kwargs):
    self.stdout.write("Generating Stripe Products")
    generators = Generator.objects.all()
    for gen in generators:
      response = stripe.Product.delete(gen.stripe_product_id)
      Price.objects.filter(product=gen).delete()
      gen.stripe_product_id = None
      gen.save()