from django import template
import re

register = template.Library()

@register.filter(name='censor')
def censor(value):
    censor_list = ['нежелательное_слово1', 'нежелательное_слово2']  # Список слов для цензуры
    for word in censor_list:
        value = re.sub(word, '*' * len(word), value, flags=re.IGNORECASE)
    return value