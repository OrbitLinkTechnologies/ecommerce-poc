from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.base, name='base'),
]