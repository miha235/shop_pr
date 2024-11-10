from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView

from .models import Product

class ProductlistView(ListView):
    model = Product

    # app_name/<model_name>_<action>
    # catalog/product_list.html

class ProductdetailView(DetailView):
    model = Product


# Создайте новую модель блоговой записи со следующими полями:

# заголовок;
# slug (реализовать через CharField);
# содержимое;
# превью (изображение);
# дата создания;
# признак публикации;
# количество просмотров.

# Для работы с блогом реализуйте CRUD для новой модели.
# CRUD реализуйте на основе CBV (ListView, DetailView, CreateView, UpdateView, DeleteView)
# Соблюдайте нейминг шаблонов для CBV контроллеров - …_list.html, …_detail.html, …_form.html.

class ProductcreateView(CreateView):
    model = Product
    fields = ("name" , "description" , "image" , "price", "category")
    success_url = reverse_lazy ( 'catalog:product_list' )

class ProductupdateView(UpdateView):
    model = Product
    fields = ("name" , "description" , "image" , "price" , "category")
    success_url = reverse_lazy ( 'catalog:product_list' )

class ProductdeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy ( 'catalog:product_list' )


def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')
