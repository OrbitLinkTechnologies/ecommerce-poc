from decouple import config
from ecommerce.models import KitchenAndHomeAppliance
from django.core.management.base import BaseCommand
from django.db import transaction
import stripe
stripe.api_key = config('STRIPE_SECRET_KEY')

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