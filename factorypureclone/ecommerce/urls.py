from django.urls import path
from . import views
#from ecommerce.views import CategoryResultsListView

app_name = 'ecommerce'

urlpatterns = [
    path('', views.category_results, name='category_results'),
    path('item/<int:id>/', views.item_page, name='item_page'),
    path('cart/', views.cart_page, name='cart_page'),
    path('remove_item_from_cart/<int:product_in_user_cart>/', views.remove_item_from_cart, name='remove_item_from_cart'),
    path('add_item_to_cart/<int:id>/', views.add_item_to_cart, name='add_item_to_cart'),
    #path('', CategoryResultsListView.as_view()),
]