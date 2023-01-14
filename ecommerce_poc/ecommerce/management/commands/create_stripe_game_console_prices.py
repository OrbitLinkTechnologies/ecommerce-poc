from ecommerce.models import Price, GameConsole
from django.core.management.base import BaseCommand
from django.db import transaction
import random
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

  help = "Generates Game Console Stripe Prices for Test Data"

  @transaction.atomic
  def handle(self, *args, **kwargs):
    self.stdout.write("Generating Generator Stripe Prices")

    # we need to generate a stripe_price_id and price => they are char and integer fields respectively
    game_consoles = GameConsole.objects.all()
    for game_console in game_consoles:
      # the random integer is going to be the unit price in cents, so we need to divide by 100 to get the dollar amount
      random_integer = random.randint(17500, 100000)
      response = stripe.Price.create(
        unit_amount = random_integer,
        currency = "usd",
        product = game_console.stripe_product_id
      )
      Price.objects.create(product=game_console, stripe_price_id=response.id, price=response.unit_amount)