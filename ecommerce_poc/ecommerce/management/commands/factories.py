import factory
from factory.django import DjangoModelFactory
from faker import Faker
fake = Faker()
import factory.fuzzy

from ecommerce.models import Generator

class GeneratorFactory(DjangoModelFactory):
    class Meta:
        model = Generator

    product_name = factory.fuzzy.FuzzyChoice([
      'Duro Star ' + fake.license_plate(),
      'Made Tough ' + fake.license_plate(),
      'Head Spinner ' + fake.license_plate(),
      'Glory Seeker ' + fake.license_plate(),
      'Metal Motivator ' + fake.license_plate(),
      'Lucky Streak ' + fake.license_plate(),
      'Live Well ' + fake.license_plate(),
      'Heavy Hitter ' + fake.license_plate(),
      'Lazy Sunday ' + fake.license_plate(),
      'Star Gazer ' + fake.license_plate(),
      'Star Seeker ' + fake.license_plate(),
      'Heavenly ' + fake.license_plate(),
      'Man\'s Best Friend ' + fake.license_plate(),
      'Texas Ryder ' + fake.license_plate(),
      'Clean Emissions ' + fake.license_plate(),
      'Tailgate ' + fake.license_plate(),
      'Rough Rider ' + fake.license_plate(),
    ])
    product_category = 'generator'
    product_manufacturer = factory.fuzzy.FuzzyChoice([
      'Cheap Design LLC',
      'Light Weight LLC',
      'Tip Top LLC',
      'Slow Repairs LLC',
      'Across the Atlantic LLC',
      'Domestic Imports LLC',
      'Made Well LLC',
      'Cheap Wads LLC',
      'City Slickers LLC',
      'Above and Beyond LLC',
      'Aim High Shoot Low LLC',
      'Alpha Dog LLC',
      'Once Upon a Time LLC',
      'Generator Tycoons LLC',
      'Amid the Great LLC',
      'Firm in Our Quality LLC',
      'Poor Quantity Great Quality LLC',
    ])
    product_brand = factory.fuzzy.FuzzyChoice([
      'Generac',
      'Cummins',
      'Dewalt',
      'Pulsar',
      'Paxcess',
      'Yamaha',
      'Kubota',
      'Honeywell',
      'Atima',
      'Simpson',
      'Aims Power',
      'Renogy',
      'Rockpals',
      'Trane',
      'Gentron',
      'Firman',
      'Energizer',
    ])
    # we need the SKU to be unique
    product_SKU = fake.ean(length=13)
    product_condition = factory.fuzzy.FuzzyChoice([
      'new',
      'refurbished'
    ])
    product_price = factory.fuzzy.FuzzyInteger(175, 38000)
    # we need to integrate and automate this with stripe
    product_quantity = factory.fuzzy.FuzzyInteger(1, 30)
    product_photos = factory.fuzzy.FuzzyChoice([
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen1.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen2.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen3.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen4.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen5.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen6.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen7.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen8.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen9.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen10.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen11.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen12.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen13.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen14.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen15.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen16.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gen17.jpg',
    ])
    generator_classification_type = factory.fuzzy.FuzzyChoice([
      'portable',
      'standby',
      'inverter'
    ])
    generator_fuel_type = factory.fuzzy.FuzzyChoice([
      'gasoline',
      'LP',
      'Dual Fuel',
      'Diesel',
      'Tri-Fuel',
    ])
    generator_continuous_wattage_value = factory.fuzzy.FuzzyChoice([
      1000,
      2000,
      3000,
      4000,
      5000,
      6000,
      7000,
      8000,
      9000,
      10000,
      11000,
      12000,
      13000,
      14000,
      15000,
      16000,
      17000,
      18000,
      19000,
      20000,
      21000,
      22000,
      23000,
      24000,
      25000,
      26000,
      27000,
      28000,
      29000,
      30000
    ])

product = GeneratorFactory()
product.product_name
product.product_category
product.product_manufacturer
product.product_brand
product.product_SKU
product.product_condition
product.product_price
product.product_quantity
product.product_photos
product.generator_classification_type
product.generator_fuel_type
product.generator_continuous_wattage_value