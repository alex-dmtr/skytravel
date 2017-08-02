import datetime
from django import template
from webapp.models import City

register = template.Library()


@register.simple_tag
def get_cities():
    return City.objects.all()

