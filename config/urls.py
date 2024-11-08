from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home, name='home'),
    path('', include('catalog.urls', namespace='catalog')),
    #path('contacts/', contacts, name='contacts'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
