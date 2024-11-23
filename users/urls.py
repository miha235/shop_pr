from django.urls import path
from .views import RegisterView, CustomLoginView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Регистрация пользователя
    path('login/', CustomLoginView.as_view(), name='login'),  # Логин пользователя
]
