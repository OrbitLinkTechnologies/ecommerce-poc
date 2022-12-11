from django.shortcuts import render
from ecommerce.models import Generator
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request, 'ecommerce/base.html')

def category_results(request):
    #context = {}
    #context['dataset'] = Generator.objects.all()
    product_list = Generator.objects.all().order_by('id')
    paginator = Paginator(product_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ecommerce/category_results.html', {'page_obj': page_obj})

def item_page(request, id):
    item_set = Generator.objects.filter(id=id)
    return render(request, 'ecommerce/item_page.html', {'item_set' : item_set})

'''class CategoryResultsListView(ListView):
    paginate_by = 2
    model = Generator'''

@login_required
def cart_page(request):
    cart_items = Generator.objects.filter(product_in_user_cart=request.user)
    cart_total = 0
    for item in cart_items:
        cart_total += item.product_price
    print('cart_total = ' + str(cart_total))
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
    print('cart_total = ' + str(cart_total))
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