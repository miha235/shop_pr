# blog/urls.py
from django.urls import path
from . import views
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='blogpost_list'),
    path('create/', views.BlogPostCreateView.as_view(), name='blogpost_create'),  # URL для создания поста
    path('<slug:slug>/', views.BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('<slug:slug>/update/', views.BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('<slug:slug>/delete/', views.BlogPostDeleteView.as_view(), name='blogpost_delete'),
]

