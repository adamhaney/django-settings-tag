# -*- coding: utf-8 -*-

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(name='settings')
def settings(attr):
    return getattr(settings, attr)
