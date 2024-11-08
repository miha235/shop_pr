from django import template

register = template.Library()

@register.filter()
def mymedia(data):
    """
    Преобразует путь изображения, добавляя '/media/' в начало для корректного доступа.
    """
    if data:
        return f'/media/{data}'
    return '#'
