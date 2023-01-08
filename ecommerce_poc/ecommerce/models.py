from django.db import models
from django.contrib.auth.models import User
import django_filters
from django.contrib.auth import get_user_model
from polymorphic.models import PolymorphicModel

# this is our base product model, which ALL products will have values for
class BaseProduct(PolymorphicModel):
    product_name = models.CharField(max_length=255)
    product_category = models.CharField(max_length=128)
    product_manufacturer = models.CharField(max_length=255)
    product_brand = models.CharField(max_length=255)
    product_SKU = models.CharField(max_length=32)
    # condition needs to be an enum with two choices: new and refurbished
    product_condition_choices = (
        ('new', 'new'),
        ('refurbished', 'refurbished')
    )
    product_condition = models.CharField(max_length=64, choices=product_condition_choices)
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
    # NOTE: I still want to consider the comments above, but for now I think the best idea
    # is to have the product overview be a text field
    product_overview = models.TextField(null=True, blank=True)
    product_features = models.JSONField(null=True, blank=True)
    product_specifications = models.JSONField(null=True, blank=True)
    # product photos and videos are s3 bucket assets as explained elsewhere
    product_photos = models.CharField(max_length=128, null=True, blank=True)
    product_videos = models.CharField(max_length=128, null=True, blank=True)
    product_discounted = models.BooleanField(default=False)
    product_discounted_rate = models.DecimalField(decimal_places=2,max_digits=5, null=True, blank=True)
    product_created_at = models.DateTimeField(auto_now_add=True)
    product_updated_at = models.DateTimeField(auto_now=True)
    stripe_product_id = models.CharField(max_length=100, blank=True, null=True)

    # we use meta inner class to set abstract to true; this means that when we run makemigrations
    # and migrate, django will not add this abstract class to the database
    class Meta:
        abstract = False

    # since we are using regular inheritance, we need this here to easily distinguish
    # our products in the base product admin view;
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
    review_title = models.CharField(max_length=255)
    review_text_body = models.TextField()
    # picture and videos are stored in s3; the fields will be strings which are paths
    # to the location of the assets within the s3 bucket
    picture_s3_url = models.CharField(max_length=128, null=True, blank=True)
    video_s3_url = models.CharField(max_length=128, null=True, blank=True)
    customer_name = models.CharField(max_length=128)
    customer_email = models.CharField(max_length=128)
    # to calculate average rating, we will add up the product ratings across the entire
    # product, and divide by the count of ratings for that product
    # this seems to be sufficient for now
    product_rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # NOTE: the reason that we create a foreign key for base product here is because
    # a review may only be associated with one product, but a product may have MANY reviews
    base_product_association = models.ForeignKey(BaseProduct, on_delete=models.CASCADE)

    def __str__(self):
        return self.review_title

class ProductQuestion(models.Model):
    customer_name = models.CharField(max_length=128)
    customer_email = models.CharField(max_length=128)
    customer_question_text_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # NOTE: we create a foreign key for base prodcut here because a
    # question may only be associated with one product, but a product,
    # may be associated with many questions
    base_product_association = models.ForeignKey(BaseProduct, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'question_' + self.customer_email

class ProductAnswer(models.Model):
    # we create the foreign key relationship here. This means that an Answer
    # can only be tied to one question, but a question can have many answers
    question = models.ForeignKey(ProductQuestion, on_delete=models.CASCADE)
    company_answer_text_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# this is going to be a one-to-one model to extend the User model
# NOTE: we need to do more investigation around OneToOneFields, ForeignKeys,
# OneToMany, and ManyToMany relationships
# it is very likely that the customer model will need to change after
# having done the aforementioned research
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
    # NOTE: we are commenting out associating a customer with a delivery for now
    # but it makes sense that customer and delivery are integrated in some way;
    # we need to be able to track our customer relationships (CRM)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # NOTE: this FK relationship says that a cart item may only be associated with
    # a single user, but a USER may be associated with ANY number of cart items, which makes sense
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
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
    # delivery needs to be associated with an invoice
    stripe_invoice_id = models.CharField(max_length=128)
    # need to store the session id of the checkout so we don't create duplicate deliveries
    stripe_checkout_session_id = models.CharField(max_length=128)
    # we have ensured that we only create a delivery if our customer successfully checks out
    # and is returned a checkout session id and a stripe invoice id to tie a delivery and an invoice together
    # we now need a field for our client to mark whether a delivery was completed or not
    # NOTE: we need to figure out a way to archive this order in stripe and mark it as read only
    # for future reference and compliance
    delivery_completed = models.BooleanField(default=False)

    def __str__(self):
      return self.user.get_username() + '_delivery'

class Price(models.Model):
  # NOTE: after doing the aforementioned research above, it may be
  # necessary to create a one to one field here. The reason for this is
  # that it does not make sense for a price to be only associated with one
  # product AND for a product to be associated with MANY prices
  # PS: it makes sense for a price to be associated with only one product
  # and for a product to be only associated with one price
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
  # NOTE: this FK relationship says that a cart item may only be associated with
  # one product and a product may be associated with many cart items
  # I think the logic of this makes sense. To abstract it even further,
  # CONSIDERING SINGLE ENTITIES: an item in someone's cart may only
  # be associated with one product (i.e. an item is not 2 products, it's only one),
  # AND a product can be in MULTIPLE different customer's carts (i.e. an
  # item can be ANY number of cart items)
  product = models.ForeignKey(BaseProduct, unique=False, on_delete=models.PROTECT)
  # NOTE: this FK relationship says that a cart item may only be associated with
  # a single user, but a USER may be associated with ANY number of cart items, which makes sense
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  orderDone = models.BooleanField(default=False)

  def __str__(self):
        return self.user.get_username() + '_' + self.product.product_name + self.product.product_SKU

# NOTE: we need to consider adding datetime_added/updated to all models that need
# to withstand retention for compliance reasons