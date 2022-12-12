import factory
from factory.django import DjangoModelFactory
import random

from ecommerce.models import Generator

class GeneratorFactory(DjangoModelFactory):
    class Meta:
        model = Generator

    product_name = factory.Faker('first_name')
    product_category = 'generator'
    product_manufacturer = factory.Faker('bs')
    product_brand = factory.Faker('company')
    product_SKU = factory.Faker('license_plate')
    product_condition = 'new'
    product_price = random.randint(0,10000)
    product_quantity = random.randint(0,25)
    product_photos = 'https://s3.amazonaws.com/ecomm-poc-fac-pu/static/images/generator_test.webp'
    generator_classification_type = 'portable'
    generator_fuel_type = 'gasoline'
    generator_continuous_wattage_value = 1000

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