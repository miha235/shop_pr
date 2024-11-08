from typing import Dict , Any

from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def product_detail(request):
    # Забираем все объекты товара
    product = Product.objects.all()
    # Передаем объект в шаблон через контекст
    context: dict[str, Any] = {'product': product}
    return render(request, 'product_detail.html', context )