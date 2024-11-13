from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from catalog import views as catalog_views  # Импортируем представления из приложения catalog под псевдонимом catalog_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name = 'home.html'), name = 'home') ,# Главная страница
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('blog/', include('blog.urls', namespace='blog')),
    path("contacts/", catalog_views.contacts, name="contacts"),  # Страница контактов в приложении catalog
    path("product/", catalog_views.ProductlistView.as_view(), name="product_list"),  # Маршрут для product_list
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)