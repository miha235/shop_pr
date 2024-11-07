from django.contrib import admin
from django.urls import path
from catalog import views  # Предположим, что ваше приложение называется catalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('catalog/product/<int:pk>/', views.product_detail, name='product_detail'),
]
