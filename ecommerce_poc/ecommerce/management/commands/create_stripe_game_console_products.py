from decouple import config
from ecommerce.models import GameConsole
from django.core.management.base import BaseCommand
from django.db import transaction
import stripe
stripe.api_key = config('STRIPE_SECRET_KEY')

class Command(BaseCommand):

  help = "Generates Game Console Stripe Products for Test Data"

  @transaction.atomic
  def handle(self, *args, **kwargs):
    self.stdout.write("Generating Game Console Stripe Products")
    game_consoles = GameConsole.objects.all()
    for game_console in game_consoles:
      response = stripe.Product.create(name = game_console.product_name)
      game_console.stripe_product_id = response.id
      game_console.save()