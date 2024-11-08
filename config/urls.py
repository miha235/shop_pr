from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from catalog import views  # Предположим, что ваше приложение называется catalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #path('', 'catalog.urls',namespace='catalog')),
    path('contacts/', views.contacts, name='contacts'),
    path('catalog/product/', views.product_detail, name='product_detail'),
]
