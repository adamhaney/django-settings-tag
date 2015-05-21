# -*- coding: utf-8 -*-

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(name='get_setting')
def get_setting(attr):
    return getattr(settings, attr)
