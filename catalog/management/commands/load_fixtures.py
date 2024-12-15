from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    help = "Загружает фикстуры и очищает старые данные"

    def handle(self, *args, **kwargs):
        # Очищаем старые данные
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Старые данные успешно очищены."))

        # Загружаем фикстуры
        try:
            call_command("loaddata", "catalog_data.json", verbosity=2)
            self.stdout.write(self.style.SUCCESS("Фикстуры успешно загружены."))
        except ObjectDoesNotExist as e:
            self.stdout.write(self.style.ERROR(f"Ошибка загрузки фикстур: {str(e)}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Произошла ошибка: {str(e)}"))
