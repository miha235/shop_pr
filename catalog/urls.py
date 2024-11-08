from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import ProductlistView, home, contacts, DogdetailView

app_name = NewappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', ProductlistView.as_view(), name = 'product_list' ),
    path('product/<int:pk>/', DogdetailView.as_view() , name = 'product_detail' ),
]
