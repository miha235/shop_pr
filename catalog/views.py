from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView , DetailView

from .models import Product

class ProductlistView(ListView):
    model = Product

    # app_name/<model_name>_<action>
    # catalog/product_list.html

class DogdetailView(DetailView):
    model = Product


def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')

#def product_list(request):
    # Забираем все объекты товара
#    catalog = Product.objects.all()
    # Передаем объект в шаблон через контекст
#    context = {'catalog': catalog}
#    return render(request, 'product_list.html', context )

def product_detail(request, pk):
    product = get_object_or_404 (Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context )