from django import template
from django.utils.safestring import SafeString

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """Adds a CSS class to a Django form field widget."""
    try:
        return field.as_widget(attrs={"class": css_class})
    except AttributeError:
        # Return the field unchanged if it's not a form field
        return field if isinstance(field, SafeString) else str(field)
