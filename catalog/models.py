from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Название категории"
    )
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]  # Сортировка категорий по имени

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="catalog/", verbose_name="Изображение")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="catalog",
        verbose_name="Категория",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    view_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]  # Сортировка продуктов по имени

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="versions"
    )
    version_name = models.CharField(max_length=100)
    version_number = models.IntegerField()
    is_current = models.BooleanField(default=False)

    def clean(self):
        # Проверка, что у продукта уже нет другой активной версии
        if self.is_current:
            active_version = Version.objects.filter(
                product=self.product, is_current=True
            ).exclude(id=self.id)
            if active_version.exists():
                raise ValidationError(
                    "У продукта уже есть активная версия. Снимите отметку с текущей версии перед назначением новой."
                )

    def save(self, *args, **kwargs):
        # Выполняем чистку перед сохранением
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.version_name} ({self.version_number})"
