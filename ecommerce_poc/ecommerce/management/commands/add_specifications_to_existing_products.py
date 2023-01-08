from ecommerce.models import KitchenAndHomeAppliance, GameConsole, Generator, SportsNutrition, HomeDecor
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
fake = Faker()

class Command(BaseCommand):

  help = "Adds json specification data to all existing products"

  @transaction.atomic
  def handle(self, *args, **kwargs):
    self.stdout.write("Generating json specification data for all existing products")

    kitchen_and_home_appliances = KitchenAndHomeAppliance.objects.all()
    for kitchen_and_home_appliance in kitchen_and_home_appliances:
      specifications = {
        'Battery' : fake.bs() + ' Lithium',
        'Motor' : fake.text() + str(fake.pyint()) + ' watts',
        'Max Weight' : str(fake.pyint()) + ' lbs',
        'Item Weight' : str(fake.pyint()) + ' once product is assembled',
        'Frame' : fake.bs(),
        'Package Contents' : [ fake.bs(), fake.bs(), fake.bs(), fake.bs() ]
      }
      kitchen_and_home_appliance.product_specifications = specifications
      kitchen_and_home_appliance.save()

    for game_console in GameConsole.objects.all():
      specifications = {
        'Memory Card' : fake.bs(),
        'Processor' : fake.bs(),
        'Battery' : fake.bs() + ' Lithium',
        'Item Weight' : str(fake.pyint()) + ' once product is assembled',
        'Max Weight' : str(fake.pyint()) + ' lbs',
        'Product Dimensions' : str(fake.pyint()) + ' x ' + str(fake.pyint()),
        'Package Contents' : [ fake.bs(), fake.bs(), fake.bs(), fake.bs(), 'HDMI Cable', 'AC Power Cord Adapter', '1 Controller']
      }
      game_console.product_specifications = specifications
      game_console.save()

    for generator in Generator.objects.all():
      specifications = {
        'Peak Watts' : fake.pyint(),
        'Running Watts' : fake.pyint(),
        'Peak Amps at 120V' : fake.pyfloat(min_value=160,max_value=300),
        'Running Amps at 120V' : fake.pyfloat(min_value=160,max_value=300),
        'Peak Amps at 240V' : fake.pyfloat(min_value=80,max_value=160),
        'Running Amps at 240V' : fake.pyfloat(min_value=80,max_value=160),
        'Voltage' : '120V / 240V',
        'Frequency' : '60Hz',
        'Engine Size' : '400 cc',
        'Engine Speed' : str(fake.pyint()) + ' rpm',
        'Fuel Type' : 'Gasoline / Propane / Natural Gas',
        'Fuel Tank Capacity' : str(fake.pyint()) + ' gallons',
        'Package Contents' : [ fake.bs(), fake.bs(), fake.bs(), fake.bs(), 'Oil Funnel', 'Battery', 'Remote Control', 'Spark Plug Wrench', 'Tool Set', 'Wheels & Handle Kit', 'Propane Regulator', 'Owner\'s Manual']
      }
      generator.product_specifications = specifications
      generator.save()
    
    for sports_and_nutrition in SportsNutrition.objects.all():
      specifications = {
        'Container Dimensions' : str(fake.pyint()) + ' x ' + str(fake.pyint()),
        'Pill Count' : fake.pyint(),
        'Flavor' : fake.text(),
        'Diet Type' : fake.text(),
        'Primary Supplement Type' : fake.text(),
        'Package Contents' : [ 'Product Container' ]
      }
      sports_and_nutrition.product_specifications = specifications
      sports_and_nutrition.save()

    for home_decor in HomeDecor.objects.all():
      specifications = {
        'Fixture Form' : fake.text(),
        'Style' : fake.text(),
        'Material' : fake.text(),
        'Color' : fake.text(),
        'Size' : 'H ' + str(fake.pyint()) + '\"  W ' + str(fake.pyint()) + "\"",
        'Installation Type' : fake.text(),
        'Finish Type' : fake.text(),
        'Item Package Quantity' : 1,
        'Max Weight' : str(fake.pyint()) + ' lbs',
        'Item Weight' : str(fake.pyint()) + ' once product is assembled',
        'Package Contents' : [ 'Home Decor Item', fake.bs(), fake.bs(), fake.bs() ]
      }
      home_decor.product_specifications = specifications
      home_decor.save()