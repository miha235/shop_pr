from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy , reverse
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView

from .models import Product

class ProductlistView(ListView):
    model = Product

    # app_name/<model_name>_<action>
    # catalog/product_list.html

class ProductdetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class ProductcreateView(CreateView):
    model = Product
    fields = ("name" , "description" , "image" , "price", "category")
    success_url = reverse_lazy ( 'catalog:product_list' )

class ProductupdateView(UpdateView):
    model = Product
    fields = ("name" , "description" , "image" , "price" , "category")
    success_url = reverse_lazy ( 'catalog:product_list' )

    def get_success_url(self):
        return reverse('catalog:product_detail',args = [self.kwargs.get('pk')])

class ProductdeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy ( 'catalog:product_list' )


def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')
