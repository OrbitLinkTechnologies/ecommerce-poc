from ecommerce.models import KitchenAndHomeAppliance, GameConsole, Generator, SportsNutrition, HomeDecor
from django.core.management.base import BaseCommand
from django.db import transaction

class Command(BaseCommand):

  help = "Adds manuals and documentation to existing all existing products"

  @transaction.atomic
  def handle(self, *args, **kwargs):
    self.stdout.write("Generating manuals and documentation to existing all existing products")

    kitchen_and_home_appliances = KitchenAndHomeAppliance.objects.all()
    for kitchen_and_home_appliance in kitchen_and_home_appliances:
      kitchen_and_home_appliance.product_manuals_and_documentation = 'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/pdfs/pizza_and_toaster_oven.pdf'
      kitchen_and_home_appliance.save()

    for game_console in GameConsole.objects.all():
      game_console.product_manuals_and_documentation = 'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/pdfs/nes_classic_edition.pdf'
      game_console.save()

    for generator in Generator.objects.all():
      generator.product_manuals_and_documentation = 'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/pdfs/generac_generator.pdf'
      generator.save()
    
    for sports_and_nutrition in SportsNutrition.objects.all():
      sports_and_nutrition.product_manuals_and_documentation = None
      sports_and_nutrition.save()

    for home_decor in HomeDecor.objects.all():
      home_decor.product_manuals_and_documentation = 'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/pdfs/chandelier.pdf'
      home_decor.save()