from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')


def product_detail(request,pk):
    # Забираем все объекты товара
    product = Product.objects.all()
    # Передаем объект в шаблон через контекст
    context = {'product': product}
    return render(request, 'product_detail.html', context )