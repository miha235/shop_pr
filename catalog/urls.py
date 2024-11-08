from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import home, contacts, product_detail, product_list

app_name = NewappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', product_list , name = 'product_list' ),
    path('product/<int:pk>/', product_detail , name = 'product_detail' ),
]
