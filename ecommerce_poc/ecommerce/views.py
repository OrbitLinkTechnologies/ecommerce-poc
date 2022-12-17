from django.shortcuts import render
from ecommerce.models import Generator
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse
from decouple import config
from django.conf import settings
from django.views.generic import TemplateView
from django.db.models import F
import stripe
stripe.api_key = config('STRIPE_SECRET_KEY')

# Create your views here.
def base(request):
    return render(request, 'ecommerce/base.html')

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
        cart_total += stripe.Price.retrieve(item.stripe_product_id).unit_amount * item.product_count_in_user_cart
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
    print('item to remove = ' + str(item_to_remove))
    cart_items = Generator.objects.filter(product_in_user_cart=request.user)
    cart_total = 0
    for item in cart_items:
        cart_total += stripe.Price.retrieve(item.stripe_product_id).unit_amount * item.product_count_in_user_cart
    return render(request, 'ecommerce/cart_page.html', {'cart_items' : cart_items,
    'cart_total' : cart_total / 100})

@login_required
def add_item_to_cart(request, id):
    item_to_add = Generator.objects.filter(id=id).update(product_in_user_cart=request.user)
    # increment the count for the item in the user's cart
    Generator.objects.filter(id=id).update(product_count_in_user_cart=F('product_count_in_user_cart') + 1)
    print('item to add = ' + str(item_to_add))
    cart_items = Generator.objects.filter(product_in_user_cart=request.user)
    cart_total = 0
    for item in cart_items:
        cart_total += stripe.Price.retrieve(item.stripe_product_id).unit_amount * item.product_count_in_user_cart
    print('cart_total = ' + str(cart_total))
    return render(request, 'ecommerce/cart_page.html', {'cart_items' : cart_items,
    'cart_total' : cart_total / 100})

def register_new_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
    print('user details are: ' + str(user))
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
        cart_total += stripe.Price.retrieve(item.stripe_product_id).unit_amount * item.product_count_in_user_cart
    print('cart_total = ' + str(cart_total))
    return render(request, 'ecommerce/checkout_page.html', {'cart_items' : cart_items,
    'cart_total' : cart_total / 100})

class CreateCheckoutSessionView(View):
  def post(self, request, *args, **kwargs):
    cart_items = Generator.objects.filter(product_in_user_cart=request.user)
    list_of_line_items = []
    for item in cart_items:
      price = item.stripe_product_id
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