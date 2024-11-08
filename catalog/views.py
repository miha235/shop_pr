from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def product_list(request):
    # Забираем все объекты товара
    products = Product.objects.all()
    # Передаем объект в шаблон через контекст
    context = {'products': products}
    return render(request, 'product_list.html', context )

def product_detail(request, pk):
    product = get_object_or_404 (Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context )