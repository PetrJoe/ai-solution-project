from django import template

register = template.Library()

@register.filter
def get_time(value):
    """Returns the time part of an agenda item (first 5 characters)"""
    return value[:5] if value else ""

@register.filter
def get_description(value):
    """Returns the description part of an agenda item (after 6th character)"""
    return value[6:] if value and len(value) > 6 else ""
