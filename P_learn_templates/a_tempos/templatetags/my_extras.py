# Create a custom filter
# Note: We can register using line A and line B below or
# We could use line C as a decorator

from django import template
#LINE A:
register = template.Library()

#LINE C:
@register.filter(name='kaato')
def cut(value, arg):
    """
    This cuts out all the values of 'arg' from the string!
    """
    return value.replace(arg, '')

# LINE B: register.filter('kaato', cut)
