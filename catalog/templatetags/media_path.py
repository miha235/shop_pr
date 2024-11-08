from django import template

register = template.Library()

@register.filter()
def mymedia(path):
    """
    Преобразует путь изображения, добавляя '/media/' в начало для корректного доступа.
    """
    if path:
        return f'/media/{path}'
    return '#'
