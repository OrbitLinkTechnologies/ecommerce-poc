from django.shortcuts import render, redirect
from ecommerce.models import Delivery, ProductQuestion, ProductAnswer, ProductReview, Customer, KitchenAndHomeAppliance, KitchenAndHomeApplianceFilter, SportsNutrition, SportsNutritionFilter, BaseProduct, Generator, GeneratorFilter, Price, GameConsole, GameConsoleFilter, HomeDecor, HomeDecorFilter, CartItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import TemplateView
from django.db.models import F
# this is temporary to get our ajax function working to do some testing, do not do this in production!
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.core.exceptions import ObjectDoesNotExist
import json
from decouple import config as dev_config
from django.conf import settings
import stripe
# NOTE: we are only going to use json config files in the future
# this is how all configuration imports will work

if settings.DEBUG == False:
  pass
else:
  with open('/etc/ecommerce_config.json') as config_file:
    config = json.load(config_file)

if settings.DEBUG == False:
  stripe.api_key = dev_config("STRIPE_SECRET_KEY")
else:
  stripe.api_key = config["STRIPE_SECRET_KEY"]

# Create your views here.
def base(request):
    return render(request, 'ecommerce/base.html')

# we are adding filtration to our category results page
# I eventually want this to replace category results page
# REMOVE THE FOLLOWING LINE IN PRODUCTION!
# NOTE: SUPER IMPORTANT!!!
# We spent around a hour to debug this;
# category did not have a default value, therefore we were getting
# a positional argument missing, since in the url
# when we go to the empty url '' (which is just localhost:8000/ecomm/)
# has no parameter set such as 'localhost:8000/ecomm/generator/'
# that matches the url parameter catcher 'localhost:8000/ecomm/<str:category>/
def filter_results_page(request, category='generator'):

  if category == 'game_console':
    return game_console_filter_results_page(request, category)
  
  if category == 'home_decor':
    return home_decor_filter_results_page(request, category)

  if category == 'sports_nutrition':
    return sports_nutrition_filter_results_page(request, category)

  if category == 'kitchen_and_home_appliance':
    return kitchen_and_home_appliance_filter_results_page(request, category)
  
  # I don't think that it's a good idea to query the entire
  # dataset each time we want to return all the possible filters
  # we need to find some way to cache this?
  all_product_brands = Generator.objects.values('product_brand').distinct().order_by()
  all_product_fuel_types = Generator.objects.values('generator_fuel_type').distinct().order_by()
  all_product_classification_types = Generator.objects.values('generator_classification_type').distinct().order_by()
  all_product_condition_types = Generator.objects.values('product_condition').distinct().order_by()

  # store all of our get variables so we have access to them in the template
  param_list = []
  if request.GET:
    for param in request.GET:
      print(param + ' = ' + str(request.GET.get(param)))
      param_list.append({
        param : request.GET.get(param)
      })

  filtered_qs = GeneratorFilter(
    request.GET,
    queryset = Generator.objects.all().order_by('id')
  ).qs
  
  paginator = Paginator(filtered_qs, 10)
  page = request.GET.get('page')

  # get the values for the filters
  product_brand = request.GET.get('product_brand')
  generator_fuel_type = request.GET.get('generator_fuel_type')
  generator_classification_type = request.GET.get('generator_classification_type')
  product_condition = request.GET.get('product_condition')

  try:
    response = paginator.page(page)
  except PageNotAnInteger:
    response = paginator.page(1)
  except EmptyPage:
    response = paginator.page(paginator.num_pages)

  generic_product_classification_types = []

  for object in all_product_classification_types:
    generic_product_classification_types.append(
      {
        'product_classification_type' : object[category + '_classification_type']
      }
    )

  return render(
    request, 'ecommerce/filter_results_page.html', 
    {
      'category' : category,
      'response' : response,
      'param_list' : param_list,
      'all_product_brands' : all_product_brands,
      'all_product_fuel_types' : all_product_fuel_types,
      'all_product_classification_types' : generic_product_classification_types,
      'all_product_condition_types' : all_product_condition_types,
      'product_brand' : [
        product_brand
      ],
      'generator_fuel_type' : [
        generator_fuel_type
      ],
      'product_classification_type' : [
        generator_classification_type
      ],
      'product_condition' : [
        product_condition
      ]
    }
  )

def game_console_filter_results_page(request, category):

  # I don't think that it's a good idea to query the entire
  # dataset each time we want to return all the possible filters
  # we need to find some way to cache this?
  all_product_brands = GameConsole.objects.values('product_brand').distinct().order_by()
  all_product_classification_types = GameConsole.objects.values('game_console_classification_type').distinct().order_by()
  all_product_condition_types = GameConsole.objects.values('product_condition').distinct().order_by()

  # store all of our get variables so we have access to them in the template
  param_list = []
  if request.GET:
    for param in request.GET:
      print(param + ' = ' + str(request.GET.get(param)))
      param_list.append({
        param : request.GET.get(param)
      })

  filtered_qs = GameConsoleFilter(
    request.GET,
    queryset = GameConsole.objects.all().order_by('id')
  ).qs
  
  paginator = Paginator(filtered_qs, 10)
  page = request.GET.get('page')

  # get the values for the filters
  product_brand = request.GET.get('product_brand')
  game_console_classification_type = request.GET.get('game_console_classification_type')
  product_condition = request.GET.get('product_condition')

  try:
    response = paginator.page(page)
  except PageNotAnInteger:
    response = paginator.page(1)
  except EmptyPage:
    response = paginator.page(paginator.num_pages)

  generic_product_classification_types = []

  for object in all_product_classification_types:
    generic_product_classification_types.append(
      {
        'product_classification_type' : object[category + '_classification_type']
      }
    )

  return render(
    request, 'ecommerce/filter_results_page.html', 
    {
      'category' : category,
      'response' : response,
      'param_list' : param_list,
      'all_product_brands' : all_product_brands,
      'all_product_classification_types' : generic_product_classification_types,
      'all_product_condition_types' : all_product_condition_types,
      'product_brand' : [
        product_brand
      ],
      'product_classification_type' : [
        game_console_classification_type
      ],
      'product_condition' : [
        product_condition
      ]
    }
  )

def home_decor_filter_results_page(request, category):

  # I don't think that it's a good idea to query the entire
  # dataset each time we want to return all the possible filters
  # we need to find some way to cache this?
  all_product_brands = HomeDecor.objects.values('product_brand').distinct().order_by()
  all_product_classification_types = HomeDecor.objects.values('home_decor_classification_type').distinct().order_by()
  all_product_condition_types = HomeDecor.objects.values('product_condition').distinct().order_by()

  # store all of our get variables so we have access to them in the template
  param_list = []
  if request.GET:
    for param in request.GET:
      print(param + ' = ' + str(request.GET.get(param)))
      param_list.append({
        param : request.GET.get(param)
      })

  filtered_qs = HomeDecorFilter(
    request.GET,
    queryset = HomeDecor.objects.all().order_by('id')
  ).qs
  
  paginator = Paginator(filtered_qs, 10)
  page = request.GET.get('page')

  # get the values for the filters
  product_brand = request.GET.get('product_brand')
  home_decor_classification_type = request.GET.get('home_decor_classification_type')
  product_condition = request.GET.get('product_condition')

  try:
    response = paginator.page(page)
  except PageNotAnInteger:
    response = paginator.page(1)
  except EmptyPage:
    response = paginator.page(paginator.num_pages)

  generic_product_classification_types = []

  for object in all_product_classification_types:
    generic_product_classification_types.append(
      {
        'product_classification_type' : object[category + '_classification_type']
      }
    )

  return render(
    request, 'ecommerce/filter_results_page.html', 
    {
      'category' : category,
      'response' : response,
      'param_list' : param_list,
      'all_product_brands' : all_product_brands,
      'all_product_classification_types' : generic_product_classification_types,
      'all_product_condition_types' : all_product_condition_types,
      'product_brand' : [
        product_brand
      ],
      'product_classification_type' : [
        home_decor_classification_type
      ],
      'product_condition' : [
        product_condition
      ]
    }
  )

def sports_nutrition_filter_results_page(request, category):

  # I don't think that it's a good idea to query the entire
  # dataset each time we want to return all the possible filters
  # we need to find some way to cache this?
  all_product_brands = SportsNutrition.objects.values('product_brand').distinct().order_by()
  all_product_classification_types = SportsNutrition.objects.values('sports_nutrition_classification_type').distinct().order_by()
  all_product_condition_types = SportsNutrition.objects.values('product_condition').distinct().order_by()

  # store all of our get variables so we have access to them in the template
  param_list = []
  if request.GET:
    for param in request.GET:
      print(param + ' = ' + str(request.GET.get(param)))
      param_list.append({
        param : request.GET.get(param)
      })

  filtered_qs = SportsNutritionFilter(
    request.GET,
    queryset = SportsNutrition.objects.all().order_by('id')
  ).qs
  
  paginator = Paginator(filtered_qs, 10)
  page = request.GET.get('page')

  # get the values for the filters
  product_brand = request.GET.get('product_brand')
  sports_nutrition_classification_type = request.GET.get('sports_nutrition_classification_type')
  product_condition = request.GET.get('product_condition')

  try:
    response = paginator.page(page)
  except PageNotAnInteger:
    response = paginator.page(1)
  except EmptyPage:
    response = paginator.page(paginator.num_pages)

  generic_product_classification_types = []

  for object in all_product_classification_types:
    generic_product_classification_types.append(
      {
        'product_classification_type' : object[category + '_classification_type']
      }
    )

  return render(
    request, 'ecommerce/filter_results_page.html', 
    {
      'category' : category,
      'response' : response,
      'param_list' : param_list,
      'all_product_brands' : all_product_brands,
      'all_product_classification_types' : generic_product_classification_types,
      'all_product_condition_types' : all_product_condition_types,
      'product_brand' : [
        product_brand
      ],
      'product_classification_type' : [
        sports_nutrition_classification_type
      ],
      'product_condition' : [
        product_condition
      ]
    }
  )

def kitchen_and_home_appliance_filter_results_page(request, category):

  # I don't think that it's a good idea to query the entire
  # dataset each time we want to return all the possible filters
  # we need to find some way to cache this?
  all_product_brands = KitchenAndHomeAppliance.objects.values('product_brand').distinct().order_by()
  all_product_classification_types = KitchenAndHomeAppliance.objects.values('kitchen_and_home_appliance_classification_type').distinct().order_by()
  all_product_condition_types = KitchenAndHomeAppliance.objects.values('product_condition').distinct().order_by()

  # store all of our get variables so we have access to them in the template
  param_list = []
  if request.GET:
    for param in request.GET:
      print(param + ' = ' + str(request.GET.get(param)))
      param_list.append({
        param : request.GET.get(param)
      })

  filtered_qs = KitchenAndHomeApplianceFilter(
    request.GET,
    queryset = KitchenAndHomeAppliance.objects.all().order_by('id')
  ).qs
  
  paginator = Paginator(filtered_qs, 10)
  page = request.GET.get('page')

  # get the values for the filters
  product_brand = request.GET.get('product_brand')
  kitchen_and_home_appliance_classification_type = request.GET.get('kitchen_and_home_appliance_classification_type')
  product_condition = request.GET.get('product_condition')

  try:
    response = paginator.page(page)
  except PageNotAnInteger:
    response = paginator.page(1)
  except EmptyPage:
    response = paginator.page(paginator.num_pages)

  generic_product_classification_types = []

  for object in all_product_classification_types:
    generic_product_classification_types.append(
      {
        'product_classification_type' : object[category + '_classification_type']
      }
    )

  return render(
    request, 'ecommerce/filter_results_page.html', 
    {
      'category' : category,
      'response' : response,
      'param_list' : param_list,
      'all_product_brands' : all_product_brands,
      'all_product_classification_types' : generic_product_classification_types,
      'all_product_condition_types' : all_product_condition_types,
      'product_brand' : [
        product_brand
      ],
      'product_classification_type' : [
        kitchen_and_home_appliance_classification_type
      ],
      'product_condition' : [
        product_condition
      ]
    }
  )

def getModel(category):
  if category == 'generator':
    return Generator
  elif category == 'home_decor':
    return HomeDecor
  elif category == 'game_console':
     return GameConsole
  elif category == 'sports_nutrition':
    return SportsNutrition
  elif category == 'kitchen_and_home_appliance':
    return KitchenAndHomeAppliance
  else:
    return ObjectDoesNotExist

# we want to set the default value here to avoid problems explained
# above the filter_results_page method
def item_page(request, id, category='generator'):
    item_set = getModel(category).objects.filter(id=id)
    product_features = item_set.first().product_features
    product_specifications = item_set.first().product_specifications
    build_variables = []
    build_variables.append(
      {
        'item_set' : item_set
      }
    )
    build_variables.append(
      {
        'category' : category
      }
    )
    for item in product_features:
      build_variables.append(
        {
          item : product_features[item]
        }
      )
    build_specification_list = []
    for spec in product_specifications:
      build_specification_list.append(
        {
          spec : product_specifications[spec]
        }
      )
    package_contents_list = []
    for spec in product_specifications:
      if spec == 'Package Contents':
        package_contents_list.append(product_specifications[spec])

    product_reviews = ProductReview.objects.filter(base_product_association=getModel(category).objects.get(id=id))

    product_questions = ProductQuestion.objects.filter(base_product_association=getModel(category).objects.get(id=id))

    # this is a hashmap where we store the rating as the key;
    # as we iterate through the ratings we check to see if the rating exists
    # (i.e. the key) and increment it if it does, otherwise we add the kv to the map
    number_of_people_per_rating = {}
    sum_rating_for_this_product = 0
    number_of_ratings_for_this_product = 0
    for review in product_reviews:
      sum_rating_for_this_product += review.product_rating
      number_of_ratings_for_this_product += 1
      if review.product_rating in number_of_people_per_rating:
        number_of_people_per_rating[review.product_rating] += 1
      else:
        number_of_people_per_rating[review.product_rating] = 1

    if number_of_ratings_for_this_product == 0:
      average_rating_for_this_product = 0
    else:
      average_rating_for_this_product = sum_rating_for_this_product / number_of_ratings_for_this_product

    # print('average = ' + str(average_rating_for_this_product))
    print('number of ratings per rating value = ' + str(number_of_people_per_rating))

    # we need to send everything into our django templates as a list
    # therefore we need to store our number_of_people_per_ratings "object"
    # within a list to be able to access it within our template
    list_of_number_of_ratings_per_rating_value = []
    list_of_number_of_ratings_per_rating_value.append(number_of_people_per_rating)

    ones_ratings = 0
    twos_ratings = 0
    threes_ratings = 0
    fours_ratings = 0
    fives_ratings = 0

    for kv in number_of_people_per_rating:
      if kv == 1:
        ones_ratings = number_of_people_per_rating[kv]
      if kv == 2:
        twos_ratings = number_of_people_per_rating[kv]
      if kv == 3:
        threes_ratings = number_of_people_per_rating[kv]
      if kv == 4:
        fours_ratings = number_of_people_per_rating[kv]
      if kv == 5:
        fives_ratings = number_of_people_per_rating[kv]

    print(ones_ratings)
    print(twos_ratings)
    print(threes_ratings)
    print(fours_ratings)
    print(fives_ratings)

    return render(request, 'ecommerce/item_page_2.html', {'build_variables' : build_variables,
    'product_specifications' : build_specification_list, 'package_contents' : package_contents_list,
    'item_id' : id, 'category' : category, 'product_reviews' : product_reviews,
    'average_rating' : str(round(average_rating_for_this_product, 2)), 'rating_count' : number_of_ratings_for_this_product,
    'ones_ratings' : ones_ratings, 'twos_ratings' : twos_ratings, 'threes_ratings' : threes_ratings,
    'fours_ratings' : fours_ratings, 'fives_ratings' : fives_ratings, 'product_questions' : product_questions})

@login_required
def cart_page(request):
    list_of_cart_items = CartItem.objects.filter(user=User.objects.get(id=request.user.id))
    cart_total = 0
    cart_items = []
    list_of_item_quantities = []
    for item in list_of_cart_items:
      list_of_item_quantities.append(item.quantity)
      price = Price.objects.get(product=item.product)
      current_item_to_append = getModel(item.product.product_category).objects.get(id=item.product.id)
      # quick little hack to add our per item total and quantity to the current
      # list's item so that we can easily access these items on the cart page
      current_item_to_append.quantity = item.quantity
      current_item_to_append.cart_item_total = price.price * item.quantity
      cart_items.append(current_item_to_append)
      cart_total += price.price * item.quantity
    return render(request, 'ecommerce/cart_page.html', {'cart_items' : cart_items,
    'cart_total' : cart_total / 100, 'quantities' : list_of_item_quantities})

@login_required
def remove_item_from_cart(request, id):
    cart_item_query_set = CartItem.objects.filter(product=BaseProduct.objects.get(id=id), user=User.objects.get(id=request.user.id))
    if cart_item_query_set.exists():
      cart_item_query_set.update(quantity=F('quantity') - 1)
      if cart_item_query_set.first().quantity <= 0:
        cart_item_query_set.first().delete()
    else:
      CartItem.objects.create(product=BaseProduct.objects.get(id=id), user=User.objects.get(id=request.user.id))
    return redirect('/ecomm/' + request.GET.get('current_view') + '/')

@login_required
def add_item_to_cart(request, id):
    cart_item_query_set = CartItem.objects.filter(product=BaseProduct.objects.get(id=id), user=User.objects.get(id=request.user.id))
    if cart_item_query_set.exists():
      cart_item_query_set.update(quantity=F('quantity') + request.POST.get('item_page_quantity_to_add'))
    else:
      CartItem.objects.create(product = BaseProduct.objects.get(id=id), user = User.objects.get(id=request.user.id), quantity = request.POST.get('item_page_quantity_to_add'))
    return redirect('/ecomm/cart/')

def register_new_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    repeat_password = request.POST.get('repeat_password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    # if we don't add the / here in front of registartion it will be treated as a relative url
    # which means that it will append the specified path parameter to the current url path
    # I had to specify ecomm, where the route "register_done" calls the
    # view stored under ecommerce templates at ecommerce/register_done.html
    return redirect('/ecomm/register_done', username=username)

def register_done(request):
    return render(request, 'ecommerce/register_done.html')

@login_required
def user_checkout(request):
    list_of_cart_items = CartItem.objects.filter(user=User.objects.get(id=request.user.id))
    cart_total = 0
    cart_items = []
    list_of_item_quantities = []
    for item in list_of_cart_items:
      list_of_item_quantities.append(item.quantity)
      price = Price.objects.get(product=item.product)
      current_item_to_append = getModel(item.product.product_category).objects.get(id=item.product.id)
      # quick little hack to add our per item total and quantity to the current
      # list's item so that we can easily access these items on the cart page
      current_item_to_append.quantity = item.quantity
      current_item_to_append.cart_item_total = price.price * item.quantity
      current_item_to_append.price = price.price
      cart_items.append(current_item_to_append)
      cart_total += price.price * item.quantity
    return render(request, 'ecommerce/checkout_page.html', {'cart_items' : cart_items,
    'cart_total' : cart_total / 100, 'quantities' : list_of_item_quantities})

@login_required
def collect_delivery_info(request):
  # we are going to utilize sessions here to pass along our delivery information,
  # once the payment is processed via stripe, we will use this information to
  # send an email to the customer, as well as store a permanent record
  # for shipping the item to the customer, as well as compliance

  # NOTE: we need to pass flow to the stripe payment processing session
  return redirect('/ecomm/create-checkout-session')

class CreateCheckoutSessionView(View):
  def post(self, request, *args, **kwargs):
    list_of_cart_items = CartItem.objects.filter(user=User.objects.get(id=request.user.id))
    list_of_line_items = []
    if request.POST:
      delivery_info = request.POST
      request.session['delivery_info'] = delivery_info
    for item in list_of_cart_items:
      
      list_of_line_items.append(
        {
          'price' : Price.objects.get(product=item.product).stripe_price_id,
          'quantity' : item.quantity
        }
      )

    list_of_product_ids_and_prices = []
    for item in list_of_cart_items:
      
      list_of_product_ids_and_prices.append(
        {
          'product' : item.product.stripe_product_id,
          'price' : Price.objects.get(product=item.product).price * item.quantity
        }
      )
    # the following domain is just a placeholder
    domain = 'https://sauerwebsites.com'
    if settings.DEBUG == False:
      domain = 'http://127.0.0.1:8000'
    checkout_session = stripe.checkout.Session.create(
      expand = ['line_items'], # this is supposed to give us access to line
      # items in the response of this checkout session, but it doesn't persist
      # after we redirect to another url such as below
      payment_method_types = ['card'],
      invoice_creation = { "enabled" : True },
      line_items = list_of_line_items,
      mode = 'payment',
      success_url = domain + '/ecomm/payment_success/?session_id={CHECKOUT_SESSION_ID}&id=' + str(request.user.id),
      cancel_url = domain + '/ecomm/payment_cancel/'
    )
    return redirect(checkout_session.url)

def successful_payment(request):

  stripe_checkout_session_response = stripe.checkout.Session.retrieve(request.GET.get('session_id'))

  if Delivery.objects.filter(stripe_checkout_session_id=request.GET.get('session_id')).exists():
    pass
  else:
    if request.session['delivery_info']:
      Delivery.objects.create(user=User.objects.get(id=request.user.id), first_name=request.session['delivery_info'].get('first_name'),
      last_name=request.session['delivery_info'].get('last_name'), email=request.session['delivery_info'].get('email'), phone_number=request.session['delivery_info'].get('phone_number'),
      address=request.session['delivery_info'].get('address'), address_extended=request.session['delivery_info'].get('address_extended'),
      city=request.session['delivery_info'].get('city'), postal_code=request.session['delivery_info'].get('postal_code'),
      country=request.session['delivery_info'].get('country'), state_or_province=request.session['delivery_info'].get('state_or_province'),
      stripe_invoice_id=stripe_checkout_session_response.invoice, stripe_checkout_session_id=stripe_checkout_session_response.id)

  # an asynchronous webhook happens around this point in our payment
  # flow that sends an email to our customer. We still need to figure
  # out an ERP (enterprise resource planning) integration for our client
  # to be able to update their resources accordingly.
  # NOTE: This needs to happen inside the webhook handling on our server
  # to avoid any race conditions

  # we aren't currently using the session_id get parameter, but left for future reference

  # notice how we use user_id, since cart item excepts to be passed a User object,
  # we can override this by the _id and specifying the id of the User
  CartItem.objects.filter(user_id = request.GET.get('id')).delete()

  return render(request, 'payment_success.html')

@csrf_exempt
def send_receipt(request):
  payload = request.body
  event = None

  try:
    event = stripe.Event.construct_from(
      json.loads(payload), stripe.api_key
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)

  # Handle the event
  if event.type == 'invoice.payment_succeeded':

    invoice_item = event.data.object # contains a stripe.Invoice
    send_customer_invoice(request, invoice_item)

    # we need to delete the item from our user's cart,
    # I feel like the best way to do that is here, because of race conditions,
    # but currently this approach is not working

  else:
    pass

  return HttpResponse(status=200)

class CancelView(TemplateView):
  
  template_name = 'payment_cancel.html'

def about_page(request):
  return render(request, 'ecommerce/about_page.html')

def contact_us_page(request):
  return render(request, 'ecommerce/contact_us_page.html')

def send_customer_question(request):
  if settings.DEBUG == False:
    from_email= dev_config("FROM_EMAIL")
    to_emails= dev_config("TO_EMAIL")
  else:
    from_email= config["FROM_EMAIL"]
    to_emails= config["TO_EMAIL"]
  send_mail = Mail(
    from_email=from_email,
    to_emails=to_emails,
    subject=request.POST['subject'],
    html_content= 'You have a message from ' + request.POST['name'] + '!<br><br>' +
    'Please respond to them @ ' + request.POST['email'] + '!<br><br>' +
    'Message Body: <br><br>' + request.POST['message']
  )
  try:
    if settings.DEBUG == False:
      sg = SendGridAPIClient(dev_config("SENDGRID_API_KEY"))
    else:
      sg = SendGridAPIClient(config["SENDGRID_API_KEY"])
    response = sg.send(send_mail)
    print(response.status_code)
    print(response.body)
    print(response.headers)

  except Exception as e:
    print(e.message)
  
  # if customer wants a copy, send them an email as well
  if request.POST.get('mail_customer_a_copy'):
    if settings.DEBUG == False:
      from_email= dev_config("FROM_EMAIL")
    else:
      from_email= config["FROM_EMAIL"]
    send_mail = Mail(
      from_email= from_email,
      to_emails= request.POST.get('email'),
      subject=request.POST['subject'],
      html_content= 'CUSTOMER COPY:<br><br>' +
      'You have a message from ' + request.POST['name'] + '!<br><br>' +
      'Please respond to them @ ' + request.POST['email'] + '!<br><br>' +
      'Message Body: <br><br>' + request.POST['message']
    )
    try:
      if settings.DEBUG == False:
        sg = SendGridAPIClient(dev_config("SENDGRID_API_KEY"))
      else:
        sg = SendGridAPIClient(config["SENDGRID_API_KEY"])
      response = sg.send(send_mail)
      print(response.status_code)
      print(response.body)
      print(response.headers)

    except Exception as e:
      print(e.message)

  return redirect('/ecomm/contact_us_page_success', name = request.POST['name'])

def contact_us_page_success(request):
  return render(request, 'ecommerce/contact_us_page_success.html', { 
    'email_from' : 'Travis\' Primary Contact Email'
    })

def send_customer_invoice(request, invoice_item):
  if settings.DEBUG == False:
    from_email = dev_config("FROM_EMAIL")
  else:
    from_email = config["FROM_EMAIL"]
  send_mail = Mail(
    from_email = from_email,
    to_emails = invoice_item.customer_email,
    subject = 'Receipt From Sauer Websites Purchase',
    html_content = 'Here is your receipt for your recent purchase at Sauer Websites Ecommerce POC: '
    + invoice_item.hosted_invoice_url + '<br><br>' +
    'You can also download the PDF directly here: ' + invoice_item.invoice_pdf + '<br><br>' +
    'This email is auto-generated by a webhook on my server that waits for a specific Stripe event to be triggered.' +
    ' Please feel free to utilize an open-source vulnerability scanner such as https://virustotal.com to confirm that there are no threats.'
  )
  try:
    if settings.DEBUG == False:
      sg = SendGridAPIClient(dev_config("SENDGRID_API_KEY"))
    else:
      sg = SendGridAPIClient(config["SENDGRID_API_KEY"])
    response = sg.send(send_mail)
    print(response.status_code)
    print(response.body)
    print(response.headers)

  except Exception as e:
    print(e.message)

def leave_review(request, id, category):
  review_title = request.POST.get('review_title')
  review_text_body = request.POST.get('review_text_body')
  customer_name = request.POST.get('customer_name')
  customer_email = request.POST.get('customer_email')
  if request.POST.get('product_rating'):
    product_rating = request.POST.get('product_rating')
  else:
    product_rating = 5

  print(str(request.POST))
  ProductReview.objects.create(review_title=review_title, review_text_body=review_text_body, customer_name=customer_name,
  customer_email=customer_email, product_rating=product_rating, base_product_association=getModel(category).objects.get(id=id))

  return redirect('/ecomm/item/' + str(id) + '/' + str(category) + '/')

def leave_question(request, id, category):
  customer_name = request.POST.get('customer_name')
  customer_email = request.POST.get('customer_email')
  customer_question_text_body = request.POST.get('customer_question_text_body')

  print(str(request.POST))
  ProductQuestion.objects.create(customer_name=customer_name, customer_email=customer_email,
  customer_question_text_body=customer_question_text_body,
  base_product_association=getModel(category).objects.get(id=id))

  return redirect('/ecomm/item/' + str(id) + '/' + str(category) + '/')