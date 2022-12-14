from django.shortcuts import render
from ecommerce.models import Generator
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect

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
        cart_total += item.product_price
    return render(request, 'ecommerce/cart_page.html', {'cart_items' : cart_items,
    'cart_total' : cart_total})

@login_required
def remove_item_from_cart(request, product_in_user_cart):
    item_to_remove = Generator.objects.filter(id=product_in_user_cart).update(product_in_user_cart=None)
    print('item to remove = ' + str(item_to_remove))
    cart_items = Generator.objects.filter(product_in_user_cart=request.user)
    cart_total = 0
    for item in cart_items:
        cart_total += item.product_price
    return render(request, 'ecommerce/cart_page.html', {'cart_items' : cart_items,
    'cart_total' : cart_total})

@login_required
def add_item_to_cart(request, id):
    item_to_add = Generator.objects.filter(id=id).update(product_in_user_cart=request.user)
    print('item to remove = ' + str(item_to_add))
    cart_items = Generator.objects.filter(product_in_user_cart=request.user)
    cart_total = 0
    for item in cart_items:
        cart_total += item.product_price
    print('cart_total = ' + str(cart_total))
    return render(request, 'ecommerce/cart_page.html', {'cart_items' : cart_items,
    'cart_total' : cart_total})

def register_new_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
    print('user details are: ' + str(user))
    # if we don't add the / here in front of registartion it will be treated as a relative url
    # which means that it will append the specified path parameter to the current url path
    # I had to specify ecomm, where the route "register_done" is which calls the
    # view stored under ecommerce templates at ecommerce/register_done.html
    return redirect('/ecomm/register_done', username=username)

def register_done(request):
    return render(request, 'ecommerce/register_done.html')

@login_required
def user_checkout(request):
    cart_items = Generator.objects.filter(product_in_user_cart=request.user)
    cart_total = 0
    for item in cart_items:
        cart_total += item.product_price
    print('cart_total = ' + str(cart_total))
    return render(request, 'ecommerce/checkout_page.html', {'cart_items' : cart_items,
    'cart_total' : cart_total})