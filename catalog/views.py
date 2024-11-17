from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy , reverse
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import Product
from .forms import ProductForm
from .models import Version
from .forms import VersionForm

class ProductlistView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'  # Назначаем контекстное имя для списка продуктов

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context['products']:
            product.current_version = product.versions.filter(is_current=True).first()
        return context


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
    form_class = ProductForm
    # fields = ("name", "description", "image", "price", "category")
    success_url = reverse_lazy ( 'catalog:product_list' )

class ProductupdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ("name" , "description" , "image" , "price" , "category")
    success_url = reverse_lazy ( 'catalog:product_list' )

    def get_success_url(self):
        return reverse('catalog:product_detail',args = [self.kwargs.get('pk')])

class ProductdeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy ( 'catalog:product_list' )

class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_initial(self):
        initial = super().get_initial()
        product_id = self.request.GET.get("product")
        if product_id:
            product = get_object_or_404(Product, pk=product_id)
            initial['product'] = product
        return initial

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')


