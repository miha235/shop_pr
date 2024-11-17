from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import ProductlistView,home,contacts,ProductdetailView,ProductcreateView, \
    ProductupdateView,ProductdeleteView,VersionCreateView

app_name = NewappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', ProductlistView.as_view(), name = 'product_list' ),
    path('product/<int:pk>/', ProductdetailView.as_view() , name = 'product_detail' ),
    path('product/create', ProductcreateView.as_view(), name = 'product_create'),
    path('product/<int:pk>/update', ProductupdateView.as_view(), name = 'product_update'),
    path('product/<int:pk>/delete', ProductdeleteView.as_view(), name = 'product_delete'),
    path('version/create/', VersionCreateView.as_view(), name='version_create'),
]
