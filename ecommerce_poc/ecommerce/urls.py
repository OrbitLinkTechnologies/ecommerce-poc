from django.urls import path
from . import views
from .views import (
  CreateCheckoutSessionView,
  SuccessView,
  CancelView
)

app_name = 'ecommerce'

urlpatterns = [
    # path('', views.category_results, name='category_results'),
    path('', views.filter_results_page, name='filter_results_page_home'),
    path('item/<int:id>/', views.item_page, name='item_page'),
    path('cart/', views.cart_page, name='cart_page'),
    path('remove_item_from_cart/<int:product_in_user_cart>/', views.remove_item_from_cart, name='remove_item_from_cart'),
    path('add_item_to_cart/<int:id>/', views.add_item_to_cart, name='add_item_to_cart'),
    path('register_new_user/', views.register_new_user, name='register_new_user'),
    path('register_done/', views.register_done, name='register_done'),
    path('user_checkout/', views.user_checkout, name='user_checkout'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('payment_success/', SuccessView.as_view(), name='payment_success'),
    path('payment_cancel/', CancelView.as_view(), name='payment_cancel'),
    path('filter_results_page/', views.filter_results_page, name='filter_results_page'),
    path('ajax_filter_results/', views.ajax_filter_results, name='ajax_filter_results'),
]