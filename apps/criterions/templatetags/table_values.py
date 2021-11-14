# Users/amount_values.py
from django import template

register = template.Library()


# Not Used this section
@register.filter(name='imgtype')
def imageType(filetype):
    filename = str(filetype)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.svg', '.apng', '.pjp', '.webp')):
        result = True
    else:
        result = False
    return result


@register.filter(name='imgpdftype')
def imagePdfType(filetype):
    filename = str(filetype)
    if filename.lower().endswith(('.pdf', '.png', '.jpg', '.jpeg', '.bmp', '.gif', '.svg', '.apng', '.pjp', '.webp')):
        result = True
    else:
        result = False
    return result


@register.filter(name='converttoint')
def converttoInt(number):
    num = int(number)
    return num


@register.filter(name='string_of')
def string_of(txt):
    text = str(txt)
    return text
