import jsonfield
from django.db import models
from django.contrib.auth.models import User
import django_filters
from django.contrib.auth import get_user_model
from polymorphic.models import PolymorphicModel

# this is our base product model, which ALL products will have values for
class BaseProduct(PolymorphicModel):
    product_name = models.CharField(max_length=255)
    product_category_choices = (
        ('generator', 'generator'),
        ('wood_stove', 'wood_stove'),
        ('pellet_stove', 'pellet_stove'),
        ('power_equipment', 'power_equipment'),
        ('mobility_scooter', 'mobility_scooter'),
        ('water_heater', 'water_heater'),
        ('electronic', 'electronic'),
        ('air_control', 'air_control')
    )
    product_category = models.CharField(max_length=128, choices=product_category_choices)
    # had to comment out color choices below until we update our models
    '''product_color_choices = (
        ('red', 'red'),
        ('yelow', 'yellow'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('orange', 'orange'),
        ('purple', 'purple'),
        ('black', 'black'),
        ('grey', 'grey'),
    )
    product_color = models.CharField(max_length=32, choices=product_color_choices)'''
    product_manufacturer = models.CharField(max_length=255)
    product_brand = models.CharField(max_length=255)
    product_SKU = models.CharField(max_length=32)
    # condition needs to be an enum with two choices: new and refurbished
    product_condition_choices = (
        ('new', 'new'),
        ('refurbished', 'refurbished')
    )
    product_condition = models.CharField(max_length=64, choices=product_condition_choices)
    # we need to remove product price, as we are only using stripe product price
    # product_price = models.DecimalField(decimal_places=2,max_digits=8)
    product_reviews = models.ForeignKey('ProductReview', on_delete=models.CASCADE, null=True, blank=True)
    product_in_stock = models.BooleanField(default=True)
    product_quantity = models.IntegerField()
    product_on_sale = models.BooleanField(default=False)
    # manufacturer and extended warranties are going to be assets stored in s3 buckets;
    # so their field values will be strings that correlate to the full path of their
    # locations within the s3 bucket; these assets will be used as attachments where
    # product manuals and documentation are needed
    product_manuals_and_documentation = models.CharField(max_length=128, null=True, blank=True)
    # any fields of our product model that I feel should be just a text field,
    # should probably be a jsonfield. It may have a higher learning curve depending upon
    # the experience of the admin, but overall I think it provides better
    # scalability and maintainability
    product_overview = jsonfield.JSONField(null=True, blank=True)
    # NOTE: null=True and blank=True are both needed her in order for us to be able to not set values
    product_question = models.ForeignKey('ProductQuestion', on_delete=models.CASCADE, null=True, blank=True)
    product_features = jsonfield.JSONField(null=True, blank=True)
    product_specifications = jsonfield.JSONField(null=True, blank=True)
    # product warranty will be a json field that we can use to display warranty information where
    # applicable on the site; NOTE: having this warranty json field is needed where we
    # want to be able to show warranty information and the pdfs from manuals and documentation won't suffice
    product_warranty_additional_information = jsonfield.JSONField(null=True, blank=True)
    # product photos and videos are s3 bucket assets as explained elsewhere
    product_photos = models.CharField(max_length=128, null=True, blank=True)
    product_videos = models.CharField(max_length=128, null=True, blank=True)
    product_discounted = models.BooleanField(default=False)
    product_discounted_rate = models.DecimalField(decimal_places=2,max_digits=5, null=True, blank=True)
    product_package_contents = jsonfield.JSONField(null=True, blank=True)
    product_created_at = models.DateTimeField(auto_now_add=True)
    product_updated_at = models.DateTimeField(auto_now=True)
    stripe_product_id = models.CharField(max_length=100, blank=True, null=True)

    # we use meta inner class to set abstract to true; this means that when we run makemigrations
    # and migrate, django will not add this abstract class to the database
    class Meta:
        abstract = False

    # since we are using regular inheritance, we need this here to easily distinguish
    # our products in the baseproduct admin view;
    # NOTE: we do not need to run makemigrations or migrate if we override or change
    # our existing overriding string method; it is only used by django internally
    # and doesn't affect our database schema
    def __str__(self):
        return self.product_name + '_' + self.product_SKU + '_pk=' + str(self.pk)

class Generator(BaseProduct):
    # we may to need make this an enum with values: portable, standby, inverter
    generator_classification_choices = (
        ('portable', 'portable'),
        ('standby', 'standby'),
        ('inverter', 'inverter')
    )
    generator_classification_type = models.CharField(max_length=128, choices=generator_classification_choices)
    # enum values for generator fuel type: gasoline, LP, Dual Fuel, Diesel, Tri-Fuel
    generator_fuel_type_choices = (
        ('gasoline', 'gasoline'),
        ('LP', 'LP'),
        ('Dual Fuel', 'Dual Fuel'),
        ('Diesel', 'Diesel'),
        ('Tri-Fuel', 'Tri-Fuel')
    )
    generator_fuel_type = models.CharField(max_length=64, choices=generator_fuel_type_choices)
    # generator continuous wattage is just a placeholder value for now
    # it is possible that we need to create a one to many model for wattage (wattage needs to be its own model)
    generator_continuous_wattage_value = models.IntegerField()
    # this will set our object name within django admin; dunder methods are overriding methods
    
    def __str__(self):
        return self.product_name + '_' + self.product_SKU + '_pk=' + str(self.pk)

class GeneratorFilter(django_filters.FilterSet):
  class Meta:
    model = Generator
    # Declare all your model fields by which you will filter
    # your queryset here:
    # NOTE: fields we need to add in the future are: Review Rating and Product features
    fields = ['product_brand', 'stripe_product_id', 'generator_fuel_type', 'generator_classification_type',
    'generator_continuous_wattage_value', 'product_condition']

class GameConsole(BaseProduct):
  
  game_console_classification_type_choices = (
    ('PlayStation', 'PlayStation'),
    ('Xbox', 'Xbox'),
    ('Nintendo', 'Nintendo'),
    ('PC', 'PC'),
    ('Laptop', 'Laptop'),
    ('VR', 'VR')
  )
  game_console_classification_type = models.CharField(max_length=64, choices=game_console_classification_type_choices)

  def __str__(self):
        return self.product_name + '_' + self.product_SKU + '_pk=' + str(self.pk)

class GameConsoleFilter(django_filters.FilterSet):
  class Meta:
    model = GameConsole
    fields = ['product_brand', 'stripe_product_id', 'game_console_classification_type', 'product_condition']

class HomeDecor(BaseProduct):
  
  home_decor_classification_type_choices = (
    ('Furniture', 'Furniture'),
    ('Outdoor_and_Garden', 'Outdoor_and_Garden'),
    ('Bedding', 'Bedding'),
    ('Bath', 'Bath'),
    ('Lighting', 'Lighting'),
    ('Rugs', 'Rugs'),
    ('Windows', 'Windows'),
    ('Pillows_and_Decor', 'Pillows_and_Decor'),
    ('Art_and_Mirrors', 'Art_and_Mirrors'),
    ('Tabletop_and_Bar', 'Tabletop_and_Bar'),
    ('Storage', 'Storage'),
    ('Holidays', 'Holidays'),
    ('Gifts', 'Gifts')
  )
  home_decor_classification_type = models.CharField(max_length=64, choices=home_decor_classification_type_choices)

  def __str__(self):
        return self.product_name + '_' + self.product_SKU + '_pk=' + str(self.pk)

class HomeDecorFilter(django_filters.FilterSet):
  class Meta:
    model = HomeDecor
    fields = ['product_brand', 'stripe_product_id', 'home_decor_classification_type', 'product_condition']

class SportsNutrition(BaseProduct):
  
  sports_nutrition_classification_type_choices = (
    ('Supplements', 'Supplements'),
    ('Vitamins', 'Vitamins'),
    ('Keto', 'Keto'),
    ('Weight_Support', 'Weight_Support'),
    ('Energy', 'Energy'),
    ('Cleanse', 'Cleanse'),
    ('Muscle_Support', 'Muscle_Support'),
    ('Digestive_Support', 'Digestive_Support'),
    ('Gel', 'Gel'),
    ('Powder', 'Powder'),
    ('Capsule', 'Capsule'),
  )
  sports_nutrition_classification_type = models.CharField(max_length=64, choices=sports_nutrition_classification_type_choices)

  def __str__(self):
        return self.product_name + '_' + self.product_SKU + '_pk=' + str(self.pk)

class SportsNutritionFilter(django_filters.FilterSet):
  class Meta:
    model = SportsNutrition
    fields = ['product_brand', 'stripe_product_id', 'sports_nutrition_classification_type', 'product_condition']

class KitchenAndHomeAppliance(BaseProduct):
  
  kitchen_and_home_appliance_classification_type_choices = (
    ('Air Fryer', 'Air Fryer'),
    ('Oven', 'Oven'),
    ('Toaster', 'Toaster'),
    ('Microwave', 'Microwave'),
    ('Coffee Maker', 'Coffee Maker'),
    ('Air Conditioner', 'Air Conditioner'),
    ('Dishwasher', 'Dishwasher'),
    ('Washing Machine', 'Washing Machine'),
    ('Drying Machine', 'Drying Machine'),
    ('Water Heater', 'Water Heater'),
  )
  kitchen_and_home_appliance_classification_type = models.CharField(max_length=64, choices=kitchen_and_home_appliance_classification_type_choices)

  def __str__(self):
        return self.product_name + '_' + self.product_SKU + '_pk=' + str(self.pk)

class KitchenAndHomeApplianceFilter(django_filters.FilterSet):
  class Meta:
    model = KitchenAndHomeAppliance
    fields = ['product_brand', 'stripe_product_id', 'kitchen_and_home_appliance_classification_type', 'product_condition']

class ProductReview(models.Model):
    review_title = models.CharField(max_length=255, default=None)
    review_text_body = models.TextField(default=None)
    # picture and videos are stored in s3; the fields will be strings which are paths
    # to the location of the assets within the s3 bucket
    picture_s3_url = models.CharField(max_length=128, null=True, blank=True)
    video_s3_url = models.CharField(max_length=128, null=True, blank=True)
    customer_name = models.CharField(max_length=128, default=None)
    customer_email = models.CharField(max_length=128, default=None)
    # this is just going to be a placeholder for now until we figure out how to properly
    # label a review object. a review should have a many to one relationship with a product

    def __str__(self):
        return self.review_title

class ProductQuestion(models.Model):
    customer_name = models.CharField(max_length=128)
    customer_email = models.CharField(max_length=128)
    customer_question_text_body = models.TextField(null=True, blank=True)
    company_answer_text_body = models.TextField(null=True, blank=True)
    # email should be unique? it might be wise to find a way to to append a SKU # and product type for
    # easier administration, so for now this is just a placeholder
    
    def __str__(self):
        return 'question_' + self.questions_customer_email

# this is going to be a one-to-one model to extend the User model
class Customer(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14, null=True, blank=True)
    address = models.CharField(max_length=64, null=True, blank=True)
    address_extended = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=128, null=True, blank=True)
    state_or_province = models.CharField(max_length=128, null=True, blank=True)
    stripe_customer_id = models.CharField(max_length=128, null=True, blank=True)
    # we need to restructure our models, we need to do away with our abstract
    # BaseProduct model and instead go with basic inheritance;
    # i.e., Generator IS a Product, Scooter IS a Product, etc
    # I would also like to re-name all foreign key references according
    # to the following: name_here_FK

# our delivery model is going to be associated with our customer model only for now
# it is a many to one relationship where we need a foreign key restraint in the table
# that can only have one of an object from another table; in our case we will create the
# foreign key restraint in the delivery model
class Delivery(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    # I don't think that an email field for a delivery needs to be unique?
    # no way that this makes sense, especially since we need to persist
    # this data
    email = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=14, null=True, blank=True)
    address = models.CharField(max_length=64, null=True, blank=True)
    address_extended = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=128, null=True, blank=True)
    state_or_province = models.CharField(max_length=128, null=True, blank=True)

class Price(models.Model):
  product = models.ForeignKey(BaseProduct, on_delete=models.CASCADE)
  stripe_price_id = models.CharField(max_length=100)
  # we need to figure out how to remove price from our BaseProduct model
  # and tie our Stripe Price to our BaseProduct model
  price = models.IntegerField(default = 0)

  def get_display_price(self):
    return "{0:.2f}".format(self.price / 100)

# it is possible that we need to change our architecture in the future, but here
# is my reasoning for creating separate Price Models for each one of our
# Product Models: I don't want to slow down our queries with Polymorphic Django queries
# and I don't necessarily want to introduce the complexity of using a Generic foreign key
# both of which are described in this SO thread: https://stackoverflow.com/questions/30343212/foreignkey-field-related-to-abstract-model-in-django
# I believe we are going to go with the route of turning our BaseProduct Abstract Class into
# a IS-A relationship for regular base-class inheritance

class CartItem(models.Model):
  datetime_added = models.DateTimeField(auto_now_add=True)
  datetime_updated = models.DateTimeField(auto_now=True)
  quantity = models.IntegerField(default=1)
  product = models.ForeignKey(BaseProduct, unique=False, on_delete=models.PROTECT)
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  orderDone = models.BooleanField(default=False)

  def __str__(self):
        return self.user.get_username() + '_' + self.product.product_name + self.product.product_SKU