from decouple import config
from ecommerce.models import Price, KitchenAndHomeAppliance
from django.core.management.base import BaseCommand
from django.db import transaction
import random
import stripe
stripe.api_key = config('STRIPE_SECRET_KEY')

class Command(BaseCommand):

  help = "Generates Kitchen And Home Appliance Stripe Prices for Test Data"

  @transaction.atomic
  def handle(self, *args, **kwargs):
    self.stdout.write("Generating Kitchen And Home Appliance Stripe Prices")

    # we need to generate a stripe_price_id and price => they are char and integer fields respectively
    kitchen_and_home_appliances = KitchenAndHomeAppliance.objects.all()
    for kitchen_and_home_appliance in kitchen_and_home_appliances:
      # the random integer is going to be the unit price in cents, so we need to divide by 100 to get the dollar amount
      random_integer = random.randint(17500, 100000)
      response = stripe.Price.create(
        unit_amount = random_integer,
        currency = "usd",
        product = kitchen_and_home_appliance.stripe_product_id
      )
      Price.objects.create(product=kitchen_and_home_appliance, stripe_price_id=response.id, price=response.unit_amount)