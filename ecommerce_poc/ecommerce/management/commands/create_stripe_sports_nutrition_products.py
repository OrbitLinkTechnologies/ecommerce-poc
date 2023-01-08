from decouple import config
from ecommerce.models import SportsNutrition
from django.core.management.base import BaseCommand
from django.db import transaction
import stripe
stripe.api_key = config('STRIPE_SECRET_KEY')

class Command(BaseCommand):

  help = "Generates Sports Nutrition Stripe Products for Test Data"

  @transaction.atomic
  def handle(self, *args, **kwargs):
    self.stdout.write("Generating Sports Nutrition Stripe Products")
    sports_nutrition_objects = SportsNutrition.objects.all()
    for sports_nutrition in sports_nutrition_objects:
      response = stripe.Product.create(name = sports_nutrition.product_name)
      sports_nutrition.stripe_product_id = response.id
      sports_nutrition.save()