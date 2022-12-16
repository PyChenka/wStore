from django import template

from mailings.forms import SubscribeForm

register = template.Library()


@register.inclusion_tag('mailings/subscribe_form.html')
def subscribe_form():
    return {'subscribe_form': SubscribeForm()}