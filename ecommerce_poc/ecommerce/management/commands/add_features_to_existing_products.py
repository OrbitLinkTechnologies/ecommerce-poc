from ecommerce.models import KitchenAndHomeAppliance, GameConsole, Generator, SportsNutrition, HomeDecor
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
fake = Faker()

class Command(BaseCommand):

  help = "Adds json feature data to all existing products"

  @transaction.atomic
  def handle(self, *args, **kwargs):
    self.stdout.write("Generating json feature data for all existing products")

    kitchen_and_home_appliances = KitchenAndHomeAppliance.objects.all()
    for kitchen_and_home_appliance in kitchen_and_home_appliances:
      features = {
        'Material' : fake.text(),
        'Fabric' : fake.text(),
        'Color' : fake.text(),
        'Surface Area' : fake.text(),
        'Quality' : fake.text(),
        'Shape' : fake.text(),
        'Vintage' : fake.text(),
        'Sculpt' : fake.text(),
      }
      kitchen_and_home_appliance.product_features = features
      kitchen_and_home_appliance.save()

    for game_console in GameConsole.objects.all():
      features = {
        'Memory Size' : fake.text(),
        'Processor Speed' : fake.text(),
        'Data Type' : fake.text(),
        'Design' : fake.text(),
        'Battery Options' : fake.text(),
        'Extended Memory Slots' : fake.text(),
        'Controllers' : fake.text(),
        'Power Cord' : fake.text(),
      }
      game_console.product_features = features
      game_console.save()

    for generator in Generator.objects.all():
      features = {
        'Power' : fake.text(),
        'Fuel' : fake.text(),
        'Engine' : fake.text(),
        'Emissions Standards' : fake.text(),
        'Idle Control' : fake.text(),
        'Oil Maintenance' : fake.text(),
        'Fuel Switch' : fake.text(),
        'Power Panel' : fake.text(),
      }
      generator.product_features = features
      generator.save()
    
    for sports_and_nutrition in SportsNutrition.objects.all():
      features = {
        'FDA Approved' : fake.text(),
        'Small Size' : fake.text(),
        'Dosage Size' : fake.text(),
        'Bottle Type' : fake.text(),
        'Special Extract' : fake.text(),
        'Easily Digestible' : fake.text(),
        'Special Discount' : fake.text(),
        'Rare Item' : fake.text(),
      }
      sports_and_nutrition.product_features = features
      sports_and_nutrition.save()

    for home_decor in HomeDecor.objects.all():
      features = {
        'Special Discount' : fake.text(),
        'Great Material' : fake.text(),
        'Unique Style' : fake.text(),
        'Satisfaction Guaranteed' : fake.text(),
        'Extra Features' : fake.text(),
        'Expedited Delivery' : fake.text(),
        'Warranty' : fake.text(),
        'Amazing Offer' : fake.text(),
      }
      home_decor.product_features = features
      home_decor.save()