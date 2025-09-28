from django import template

register = template.Library()

@register.filter
def times(number):
    """Loop filter for star ratings"""
    try:
        return range(int(number))
    except (ValueError, TypeError):
        return range(0)

@register.filter
def subtract(value, arg):
    """Subtract arg from value"""
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return 0
