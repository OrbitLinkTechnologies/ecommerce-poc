import factory
from factory.django import DjangoModelFactory
from faker import Faker
fake = Faker()
import factory.fuzzy
from ecommerce.models import Generator, HomeDecor, GameConsole, SportsNutrition, KitchenAndHomeAppliance
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

class SportsNutritionFactory(DjangoModelFactory):
  class Meta:
    model = SportsNutrition

  product_name = factory.fuzzy.FuzzyChoice([
    'Arma Sport Reload: Whey Protein',
    'BulletProof Greens',
    'Sport Formula Powder Vitamin',
    'Vitamin Capsules with BCAA Amino Acids & Digestive',
    'GNC Mega Men Sport 180 Capsules',
    'All Sport Multi-Vitamin',
    'Blaze Fat Burner Supplements',
    'First Endurance Liquid Shot',
    'Spring Energy Canaberry',
    'GU Roctane Energy Gel',
    'Amino Aid BCAAs 100 tablets',
    'Biotics Probiotic Supplements',
    'Perfect Keto Collagen Protein Powder',
    'Myogenix Myovite Multivitamin',
    'Omega 3 Supplements - 90 Day',
    'BioSteel Sport Greens Pineapple',
    'Wilderness Athlete Green Infusion',
  ])

  product_category = 'sports_nutrition'

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
      'Sports Nutrition Tycoons LLC',
      'Amid the Great LLC',
      'Firm in Our Quality LLC',
      'Poor Quantity Great Quality LLC',
    ])

  product_brand = factory.fuzzy.FuzzyChoice([
      'GU',
      'NOW',
      'Clif Bar & Company',
      'Pure Encapsulations',
      'WEIDER',
      'USN',
      'Trace Minerals Research',
    ])
  # we need the SKU to be unique
  product_SKU = fake.ean(length=13)
  product_condition = factory.fuzzy.FuzzyChoice([
      'new',
      'refurbished'
    ])
  product_quantity = factory.fuzzy.FuzzyInteger(1, 30)
  product_photos = factory.fuzzy.FuzzyChoice([
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/sn_1.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/sn_2.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/sn_3.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/sn_4.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/sn_5.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/sn_6.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/sn_7.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/sn_8.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/sn_9.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/sn_10.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/sn_11.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/sn_12.jpg',
    ])
  sports_nutrition_classification_type = factory.fuzzy.FuzzyChoice([
    ('Supplements'),
    ('Vitamins'),
    ('Keto'),
    ('Weight_Support'),
    ('Energy'),
    ('Cleanse'),
    ('Muscle_Support'),
    ('Digestive_Support'),
    ('Gel'),
    ('Powder'),
    ('Capsule'),
  ])

class KitchenAndHomeApplianceFactory(DjangoModelFactory):
  class Meta:
    model = KitchenAndHomeAppliance

  product_name = factory.fuzzy.FuzzyChoice([
    'Foodi 8 Quart 6-in-1 DualZone 2-Basket Air Fryer',
    'Mini Smart Toaster Oven',
    'Smart Oven Pro Toaster Oven',
    'Countertop Toaster Oven & Pizza Maker Large 4-Slice Capacity',
    '22-Quart Roaster Oven',
    'Clear View Toaster: Extra Wide Slot Toaster with See Through Window',
    '7 in 1 Convection Toaster Oven Cooker',
    'Mini Maker Electric Round Griddle',
    'Window-Mounted Room Air Conditioner',
    'Pure Chill Evaporative Air Cooler',
    'Portable Electric Air Conditioner Unit',
    '24" Stainless Steel Built-In Dishwasher',
    'Smart Dial Front Load Washer',
    'Graphite Smart wi-fi Enabled Top Load Washer',
    'Smart Dial Electric Dryer with FlexDry',
    'Electric Compact Portable Clothes Laundry Dryer with Stainless Steel Tub',
    'Electric Kettle with Stainless Steel Filter and Inner Lid',
    'Glass Electric Tea Kettle, Water Boiler & Heater'
  ])

  product_category = 'kitchen_and_home_appliance'

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
      'Kitchen and Home Appliance Tycoons LLC',
      'Amid the Great LLC',
      'Firm in Our Quality LLC',
      'Poor Quantity Great Quality LLC',
    ])

  product_brand = factory.fuzzy.FuzzyChoice([
      'Hamilton Beach',
      'DASH',
      'Cuisinart',
      'KitchenAid',
      'Instant Pot',
      'Ninja',
      'Nostalgia',
      'Oster',
      'Frigidaire',
      'Breville',
      'Antarctic Star',
      'Arctic Air',
      'Kenmore',
      'SAMSUNG',
      'LG',
      'Panda',
      'COSORI',
    ])
  # we need the SKU to be unique
  product_SKU = fake.ean(length=13)
  product_condition = factory.fuzzy.FuzzyChoice([
      'new',
      'refurbished'
    ])
  product_quantity = factory.fuzzy.FuzzyInteger(1, 30)
  product_photos = factory.fuzzy.FuzzyChoice([
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_1.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_2.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_3.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_4.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_5.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_6.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_7.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_8.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_9.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_10.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_11.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_12.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_13.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_14.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_15.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_16.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_17.jpg',
      'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/kha_18.jpg',
    ])
  kitchen_and_home_appliance_classification_type = factory.fuzzy.FuzzyChoice([
    ('Air Fryer'),
    ('Oven'),
    ('Toaster'),
    ('Microwave'),
    ('Coffee Maker'),
    ('Air Conditioner'),
    ('Dishwasher'),
    ('Washing Machine'), 
    ('Drying Machine'),
    ('Water Heater'), 
  ])