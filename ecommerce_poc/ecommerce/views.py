from django.shortcuts import render
from ecommerce.models import KitchenAndHomeAppliance, KitchenAndHomeApplianceFilter, SportsNutrition, SportsNutritionFilter, BaseProduct, Generator, GeneratorFilter, Price, GameConsole, GameConsoleFilter, HomeDecor, HomeDecorFilter, CartItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse
from decouple import config
from django.conf import settings
from django.views.generic import TemplateView
from django.db.models import F
# this is temporary to get our ajax function working to do some testing, do not do this in production!
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
import stripe
stripe.api_key = config('STRIPE_SECRET_KEY')

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
    return render(request, 'ecommerce/item_page.html', {'item_set' : item_set,
    'category' : category})

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
    return redirect('/ecomm/cart/')

@login_required
def add_item_to_cart(request, id):
    cart_item_query_set = CartItem.objects.filter(product=BaseProduct.objects.get(id=id), user=User.objects.get(id=request.user.id))
    if cart_item_query_set.exists():
      cart_item_query_set.update(quantity=F('quantity') + 1)
    else:
      CartItem.objects.create(product=BaseProduct.objects.get(id=id), user=User.objects.get(id=request.user.id))
    return redirect('/ecomm/cart/')

def register_new_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
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

class CreateCheckoutSessionView(View):
  def post(self, request, *args, **kwargs):
    list_of_cart_items = CartItem.objects.filter(user=User.objects.get(id=request.user.id))
    list_of_line_items = []
    for item in list_of_cart_items:
      
      list_of_line_items.append(
        {
          'price' : Price.objects.get(product=item.product).stripe_price_id,
          'quantity' : item.quantity
        }
      )
    # price = Generator.objects.get(id=1)
    # the following domain is just a placeholder
    domain = 'futuredomain.com'
    if settings.DEBUG:
      domain = 'http://127.0.0.1:8000'
    checkout_session = stripe.checkout.Session.create(
      payment_method_types=['card'],
      line_items=list_of_line_items,
      mode = 'payment',
      success_url = domain + '/ecomm/payment_success/',
      cancel_url = domain + '/ecomm/payment_cancel/'
    )
    return redirect(checkout_session.url)

class SuccessView(TemplateView):
  template_name = 'payment_success.html'

class CancelView(TemplateView):
  template_name = 'payment_cancel.html'

def about_page(request):
  return render(request, 'ecommerce/about_page.html')

def contact_us_page(request):
  return render(request, 'ecommerce/contact_us_page.html')

def send_customer_question(request):
  send_mail = Mail(
    from_email= os.environ.get("FROM_EMAIL"),
    to_emails= os.environ.get("TO_EMAIL"),
    subject=request.POST['subject'],
    html_content= 'You have a message from ' + request.POST['name'] + '!<br><br>' +
    'Please respond to them @ ' + request.POST['email'] + '!<br><br>' +
    'Message Body: <br><br>' + request.POST['message']
  )
  try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
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