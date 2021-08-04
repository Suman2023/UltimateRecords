from django import template

register = template.Library()


@register.filter(name='con')
def con(value, args):
    return str(args)