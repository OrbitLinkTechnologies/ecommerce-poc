import factory
from factory.django import DjangoModelFactory
from faker import Faker
fake = Faker()
import factory.fuzzy
from ecommerce.models import Generator, HomeDecor, GameConsole
from decouple import config
import stripe
stripe.api_key = config('STRIPE_SECRET_KEY')

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

class GameConsoleFactory(DjangoModelFactory):
  class Meta:
    model = GameConsole

  product_name = factory.fuzzy.FuzzyChoice([
    'PlayStation 1',
    'PlayStation 2',
    'PlayStation 3',
    'PlayStation 4',
    'PlayStation 5',
    'Xbox',
    'Xbox 360',
    'Xbox One',
    'Nintendo Entertainment System',
    'Super Nintendo Entertainment System',
    'Nintendo 64',
    'Nintendo GameCube',
    'Nintendo Switch',
    'Meta Quest 2 VR',
    'PlayStation VR',
    'Lenovo Legion Tower 5i',
    'Alienware Aurora R13',
  ])

  product_category = 'game_console'

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
      'Game Console Tycoons LLC',
      'Amid the Great LLC',
      'Firm in Our Quality LLC',
      'Poor Quantity Great Quality LLC',
    ])

  product_brand = factory.fuzzy.FuzzyChoice([
      'Sony',
      'Microsoft',
      'Nintendo',
      'Meta',
      'Lenovo',
      'Alienware',
    ])
  # we need the SKU to be unique
  product_SKU = fake.ean(length=13)
  product_condition = factory.fuzzy.FuzzyChoice([
      'new',
      'refurbished'
    ])
  product_quantity = factory.fuzzy.FuzzyInteger(1, 30)
  product_photos = factory.fuzzy.FuzzyChoice([
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_1.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_2.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_3.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_4.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_5.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_6.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_7.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_8.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_9.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_10.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_11.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_12.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_13.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_14.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_15.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_16.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_17.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/gc_18.jpg',
    ])
  game_console_classification_type = factory.fuzzy.FuzzyChoice([
    'PlayStation',
    'Xbox',
    'Nintendo',
    'PC',
    'Laptop',
    'VR',
  ])

class HomeDecorFactory(DjangoModelFactory):
  class Meta:
    model = HomeDecor

  product_name = factory.fuzzy.FuzzyChoice([
    'Upholstered Sleeper Sofa with Sectional',
    'Roll Arm Leather Armchair',
    'Eucalyptus Double Chaise Lounge',
    'Indoor/Outdoor Concrete C-Table',
    'Cotton Comforter',
    'Sherpa Robe',
    'Round Chandelier',
    'Indoor/Outdoor Chandelier',
    'Wool Rug',
    'Outdoor Grommet Curtain',
    'Belgian Linen Pillows',
    'Rectangular Wall Mirror',
    'Forest Gnome',
    'Handwoven Tote Baskets',
    'Aspen Spruce Wreath',
    '10-Piece Champagne Set',
    'Faux Christmas Trees',
  ])

  product_category = 'home_decor'

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
      'Home Decor Tycoons LLC',
      'Amid the Great LLC',
      'Firm in Our Quality LLC',
      'Poor Quantity Great Quality LLC',
    ])

  product_brand = factory.fuzzy.FuzzyChoice([
      'West Elm',
      'Uncommon Goods',
      'Gubi',
      'HomeGoods',
      'Wayfair',
      'Jungalow',
      'Parachute',
      'The Citizenry',
      'Allform',
      'Anthropologie',
    ])
  # we need the SKU to be unique
  product_SKU = fake.ean(length=13)
  product_condition = factory.fuzzy.FuzzyChoice([
      'new',
      'refurbished'
    ])
  product_quantity = factory.fuzzy.FuzzyInteger(1, 30)
  product_photos = factory.fuzzy.FuzzyChoice([
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_1.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_2.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_3.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_4.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_5.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_6.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_7.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_8.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_9.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_10.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_11.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_12.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_13.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_14.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_15.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/hd_16.jpg',
    ])
  home_decor_classification_type = factory.fuzzy.FuzzyChoice([
    'Furniture',
    'Outdoor_and_Garden',
    'Bedding',
    'Bath',
    'Lighting',
    'Rugs',
    'Windows',
    'Pillows_and_Decor',
    'Art_and_Mirrors',
    'Tabletop_and_Bar',
    'Storage',
    'Holidays',
    'Gifts'
  ])