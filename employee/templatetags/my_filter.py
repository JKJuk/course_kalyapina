from django import template

register = template.Library()


@register.filter(name='nds')
def nds(salary, nds):
    return salary * (100 - nds) / 100
