from django.shortcuts import render
from ecommerce.models import Generator
from django.views.generic import ListView
from django.core.paginator import Paginator

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

'''class CategoryResultsListView(ListView):
    paginate_by = 2
    model = Generator'''