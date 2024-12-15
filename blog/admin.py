# blog/admin.py
from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "created_at",
        "is_published",
        "view_counter",
    )  # Правильные атрибуты
    list_filter = ("is_published",)  # Фильтрация по is_published
    search_fields = ("title", "content")

    # Если вы хотите сделать view_counter и is_published доступными как методы, можно их реализовать в модели:
    def is_published(self, obj):
        return obj.is_published

    is_published.admin_order_field = "is_published"  # Для сортировки
    is_published.short_description = "Опубликована"

    def view_counter(self, obj):
        return obj.view_counter

    view_counter.admin_order_field = "view_counter"  # Для сортировки
    view_counter.short_description = "Количество просмотров"


admin.site.register(BlogPost, BlogPostAdmin)
