from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm, PasswordRecoveryForm

import random
import string


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')  # Перенаправление на страницу входа после успешной регистрации

    def form_valid(self, form):
        # Сохранение пользователя
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        # Генерация кода подтверждения
        verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Отправка письма с кодом
        try:
            send_mail(
                'Ваш код подтверждения',
                f'Ваш код подтверждения: {verification_code}',
                settings.EMAIL_HOST_USER,  # Email отправителя из settings.py
                [user.email],  # Email получателя
                fail_silently=False,
            )
        except Exception as e:
            # Логирование или обработка ошибки
            print(f"Ошибка при отправке письма: {e}")

        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Укажите путь к вашему шаблону
    redirect_authenticated_user = False  # Отключить перенаправление
    success_url = reverse_lazy('home')  # Укажите вашу домашнюю страницу

    def get_success_url(self):
        """Переопределите метод, чтобы перенаправить пользователя после успешного входа."""
        return self.success_url


class PasswordRecoveryView(FormView):
    template_name = 'registration/recover_password.html'
    form_class = PasswordRecoveryForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = get_user_model().objects.get(email = email)
        except get_user_model().DoesNotExist:
            return redirect('password_recovery_failed')

        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k = 8))
        user.set_password(new_password)
        user.save()

        send_mail(
            'Восстановление пароля',
            f'Ваш новый пароль: {new_password}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently = False,
        )
        return super().form_valid(form)
