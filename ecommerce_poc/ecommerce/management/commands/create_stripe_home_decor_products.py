from decouple import config
from ecommerce.models import HomeDecor
from django.core.management.base import BaseCommand
from django.db import transaction
import stripe
stripe.api_key = config('STRIPE_SECRET_KEY')

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