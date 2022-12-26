from decouple import config
from ecommerce.models import Generator, Price
from django.core.management.base import BaseCommand
from django.db import transaction
import stripe
stripe.api_key = config('STRIPE_SECRET_KEY')

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