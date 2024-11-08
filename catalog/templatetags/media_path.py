from django import template
from django.conf import settings

register = template.Library()

@register.filter()
def mymedia(data):
    """
    Преобразует путь изображения, добавляя '/media/' в начало для корректного доступа.
    """
    if data:
        return f'/media/{data}'
    return '#'
