from django.urls import path
from . import views
#from ecommerce.views import CategoryResultsListView

app_name = 'ecommerce'

urlpatterns = [
    path('', views.category_results, name='category_results'),
    #path('', CategoryResultsListView.as_view()),
]