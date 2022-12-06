from django import template

register = template.Library()

# @register.filter
# def addclass(field, css):
#     """Добавляет атрибут class в теги <input> при рендеринге полей формы"""
#     return field.as_widget(attrs={'class': css})


@register.filter
def addattrs(field, css):
    """
    Добавляет атрибуты в теги <input> при рендеринге полей формы.
    Ввод в формате 'атрибут1:значение1,атрибут2:значение2,...'
    """
    attrs = {}
    definition = css.split(',')

    for d in definition:
        key, value = d.split(':')
        if key == 'placeholder':
            value = f'{value} {field.label.lower()}'
        attrs[key] = value
    return field.as_widget(attrs=attrs)


@register.filter(name='count')
def cart_count(cart):
    """Подсчитывает количество товаров в корзине в сессии"""
    return sum(cart[x]['quantity'] for x in cart)