from django.test import TestCase
from ecommerce.models import Generator

# Create your tests here.

class GeneratorTestCase(TestCase):
  def setUp(self):
    Generator.objects.create(product_name="Trusted Name", product_category="generator",
    product_manufacturer="Intel", product_brand="Sony", product_SKU="SKU_1234",
    product_condition="new", product_price=1200, product_quantity=100, generator_classification_type="portable",
    generator_fuel_type="gasoline", generator_continuous_wattage_value=10000, product_on_sale=True)

  def test_provided_and_default_generator_values(self):
    generator_1 = Generator.objects.get(product_SKU="SKU_1234")
    self.assertEqual("Trusted Name", generator_1.product_name)
    self.assertEqual("generator", generator_1.product_category)
    self.assertEqual("Intel", generator_1.product_manufacturer)
    self.assertEqual("Sony", generator_1.product_brand)
    self.assertEqual("SKU_1234", generator_1.product_SKU)
    self.assertEqual("new", generator_1.product_condition)
    self.assertEqual(1200, generator_1.product_price)
    self.assertEqual(100, generator_1.product_quantity)
    self.assertEqual("portable", generator_1.generator_classification_type)
    self.assertEqual("gasoline", generator_1.generator_fuel_type)
    self.assertEqual(10000, generator_1.generator_continuous_wattage_value)
    self.assertEqual(None, generator_1.product_in_user_cart)
    self.assertEqual(None, generator_1.product_reviews)
    self.assertEqual(True, generator_1.product_in_stock)
    self.assertTrue(generator_1.product_on_sale)
    self.assertEqual(None, generator_1.product_manuals_and_documentation)
    self.assertEqual(None, generator_1.product_overview)
    self.assertEqual(None, generator_1.product_question)
    self.assertEqual(None, generator_1.product_features)
    self.assertEqual(None, generator_1.product_warranty_additional_information)
    self.assertEqual(None, generator_1.product_photos)
    self.assertEqual(None, generator_1.product_videos)
    self.assertFalse(generator_1.product_discounted)
    self.assertEqual(None, generator_1.product_discounted_rate)