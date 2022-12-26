from django.shortcuts import render
from ecommerce.models import Generator, GeneratorFilter, Price, GameConsole, GameConsoleFilter, HomeDecor, HomeDecorFilter
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
import stripe
stripe.api_key = config('STRIPE_SECRET_KEY')

# Create your views here.
def base(request):
    return render(request, 'ecommerce/base.html')

# I'm thinking that we should create a specific function for our ajax
# requests, so that we can return JUST the filtered data and NOT
# the entire HTML document
@csrf_exempt
def ajax_filter_results(request):
  filtered_qs = GeneratorFilter(
    request.GET,
    queryset = Generator.objects.all().order_by('id')
  ).qs
  paginator = Paginator(filtered_qs, 10)
  for filtered in filtered_qs:
    print('filtered_qs = ' + str(filtered))
  page = request.GET.get('page')
  try:
    response = paginator.page(page)
  except PageNotAnInteger:
    response = paginator.page(1)
  except EmptyPage:
    response = paginator.page(paginator.num_pages)
  return redirect(
    '/ecomm/filter_results_page/?page=' + page +'&product_brand=Love-Kerr', {'response' : response}
  )

# we are adding filtration to our category results page
# I eventually want this to replace category results page
# REMOVE THE FOLLOWING LINE IN PRODUCTION!
@csrf_exempt
def filter_results_page(request, category):

  if category == 'game_console':
    return game_console_filter_results_page(request, category)
  
  if category == 'home_decor':
    return home_decor_filter_results_page(request, category)
  
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

def category_results(request):
    product_list = Generator.objects.all().order_by('id')
    paginator = Paginator(product_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ecommerce/category_results.html', {'page_obj': page_obj})

def item_page(request, id):
    item_set = Generator.objects.filter(id=id)
    return render(request, 'ecommerce/item_page.html', {'item_set' : item_set})

@login_required
def cart_page(request):
    cart_items = Generator.objects.filter(product_in_user_cart=request.user)
    cart_total = 0
    for item in cart_items:
        price = Price.objects.filter(product=item)
        for object in price:
          cart_total += object.price * item.product_count_in_user_cart
    return render(request, 'ecommerce/cart_page.html', {'cart_items' : cart_items,
    'cart_total' : cart_total / 100})

@login_required
def remove_item_from_cart(request, product_in_user_cart):
    # item_to_remove = Generator.objects.filter(id=product_in_user_cart).update(product_in_user_cart=None)
    item_to_remove = Generator.objects.filter(id=product_in_user_cart).first()
    if item_to_remove.product_count_in_user_cart == 1:
      item_to_remove.product_in_user_cart=None
      item_to_remove.product_count_in_user_cart = 0
      item_to_remove.save()
    else:
      if item_to_remove.product_count_in_user_cart > 1:
        # decrement the count for the item in the user's cart
        item_to_remove.product_count_in_user_cart=F('product_count_in_user_cart') - 1
        item_to_remove.save()
    cart_items = Generator.objects.filter(product_in_user_cart=request.user)
    cart_total = 0
    for item in cart_items:
        price = Price.objects.filter(product=item)
        for object in price:
          cart_total += object.price * item.product_count_in_user_cart
    return render(request, 'ecommerce/cart_page.html', {'cart_items' : cart_items,
    'cart_total' : cart_total / 100})

@login_required
def add_item_to_cart(request, id):
    item_to_add = Generator.objects.filter(id=id).update(product_in_user_cart=request.user)
    # increment the count for the item in the user's cart
    Generator.objects.filter(id=id).update(product_count_in_user_cart=F('product_count_in_user_cart') + 1)
    cart_items = Generator.objects.filter(product_in_user_cart=request.user)
    cart_total = 0
    for item in cart_items:
        price = Price.objects.filter(product=item)
        for object in price:
          cart_total += object.price * item.product_count_in_user_cart
    return render(request, 'ecommerce/cart_page.html', {'cart_items' : cart_items,
    'cart_total' : cart_total / 100})

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
    cart_items = Generator.objects.filter(product_in_user_cart=request.user)
    cart_total = 0
    for item in cart_items:
        price = Price.objects.filter(product=item)
        for object in price:
          cart_total += object.price * item.product_count_in_user_cart
    return render(request, 'ecommerce/checkout_page.html', {'cart_items' : cart_items,
    'cart_total' : cart_total / 100})

class CreateCheckoutSessionView(View):
  def post(self, request, *args, **kwargs):
    cart_items = Generator.objects.filter(product_in_user_cart=request.user)
    list_of_line_items = []
    for item in cart_items:
      price_query_set = Price.objects.filter(product=item)
      for unit_amount in price_query_set:
        price = unit_amount.stripe_price_id
      quantity = item.product_count_in_user_cart
      list_of_line_items.append(
        {
          'price' : price,
          'quantity' : quantity
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