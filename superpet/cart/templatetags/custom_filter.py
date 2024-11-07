from django import template

register = template.Library()

@register.filter()
def multiply(num1,num2):
    return num1*num2

@register.filter()
def div(num1,num2):
    return num1/num2
