from django.urls import path, include
from . import views
from .views import (
  CreateCheckoutSessionView,
  CancelView
)
from django.contrib.auth.views import LoginView

app_name = 'ecommerce'

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    # path('auth0/', include('social_django.urls', namespace='social')),
    path('leave_question/<int:id>/<str:category>/', views.leave_question, name='leave_question'),
    path('leave_review/<int:id>/<str:category>/', views.leave_review, name='leave_review'),
    path('send_receipt/', views.send_receipt, name='send_receipt'),
    path('collect_delivery_info/', views.collect_delivery_info, name='collect_delivery_info'),
    path('contact_us_page_success/', views.contact_us_page_success, name='send_customer_question'),
    path('send_customer_question/', views.send_customer_question, name='send_customer_question'),
    path('contact_us/', views.contact_us_page, name='contact_us_page'),
    path('about/', views.about_page, name='about_page'),
    # authlib related oauth paths
    path("", views.index, name="index"),
    path("auth0_login", views.auth0_login, name="auth0_login"),
    path("auth0_logout", views.auth0_logout, name="auth0_logout"),
    path("callback", views.callback, name="callback"),
    # auth0 related url paths, next 3 lines
    path('profile/', views.profile, name='profile'),
    #path('login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout'),
    path('item/<int:id>/<str:category>/', views.item_page, name='item_page'),
    path('cart/', views.cart_page, name='cart_page'),
    path('remove_item_from_cart/<int:id>/', views.remove_item_from_cart, name='remove_item_from_cart'),
    path('add_item_to_cart/<int:id>/', views.add_item_to_cart, name='add_item_to_cart'),
    path('register_new_user/', views.register_new_user, name='register_new_user'),
    path('register_done/', views.register_done, name='register_done'),
    path('user_checkout/', views.user_checkout, name='user_checkout'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('payment_success/', views.successful_payment, name='payment_success'),
    path('payment_cancel/', CancelView.as_view(), name='payment_cancel'),
    path('filter_results_page/<str:category>/', views.filter_results_page, name='filter_results_page'),
]