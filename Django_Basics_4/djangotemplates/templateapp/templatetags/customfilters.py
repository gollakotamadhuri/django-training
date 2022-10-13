from django import template

register = template.Library()


@register.filter(name='cut')
def cut(text, arg):
    return text.replace(arg, '')
