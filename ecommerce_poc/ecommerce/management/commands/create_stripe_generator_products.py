from decouple import config
from ecommerce.models import Generator
from django.core.management.base import BaseCommand
from django.db import transaction
import stripe
stripe.api_key = config('STRIPE_SECRET_KEY')

class Command(BaseCommand):

  help = "Generates Generator Stripe Products for Test Data"

  @transaction.atomic
  def handle(self, *args, **kwargs):
    self.stdout.write("Generating Generator Stripe Products")
    generators = Generator.objects.all()
    for gen in generators:
      response = stripe.Product.create(name = gen.product_name)
      gen.stripe_product_id = response.id
      gen.save()