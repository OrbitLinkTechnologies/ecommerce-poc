from django import template
from ecommerce.models import Generator
import json
from decouple import config as dev_config
from django.conf import settings
import stripe

if settings.DEBUG == False:
  pass
else:
  with open('/etc/ecommerce_config.json') as config_file:
    config = json.load(config_file)

if settings.DEBUG == False:
  stripe.api_key = dev_config("STRIPE_SECRET_KEY")
else:
  stripe.api_key = config["STRIPE_SECRET_KEY"]

register = template.Library()

@register.filter
def modulo(num, val):
    return num % val

@register.filter(name='times')
def times(number):
    return range(number)

# we need to re-name this filter to the price calculation for a SPECIFIC product
# times the quantity of this product in the user's cart
@register.filter
def stripe_price(item, stripe_product_id):
  price_object = stripe.Price.retrieve(stripe_product_id)
  # might need to remove the $ and not cast to a string in the future,
  # this could potentially cause a lot of problems
  print('number of items in user cart = ' + str(item.product_count_in_user_cart))
  return (item.product_count_in_user_cart * price_object.unit_amount) / 100

# we need to create a separate filter to calculate the price
# of a product, independent of the current count that is in a user's cart
@register.filter
def single_product_price(item, stripe_product_id):
  price_object = stripe.Price.retrieve(stripe_product_id)
  return price_object.unit_amount / 100

@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
  d = context['request'].GET.copy()
  for k, v in kwargs.items():
    d[k] = v
  for k in [k for k, v in d.items() if not v]:
    del d[k]
  return d.urlencode()

@register.filter
def divide(numerator, denominator):
  try:
    return int(numerator) / int(denominator)
  except (ValueError, ZeroDivisionError):
    return 'There was an error with the divide by 100 filter'