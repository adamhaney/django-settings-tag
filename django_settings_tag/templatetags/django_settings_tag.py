# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.simple_tag(name='settings')
def settings(attr):
    from django.conf import settings
    return getattr(settings, attr)
