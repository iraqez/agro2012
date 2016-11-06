from django import template
from news.models import Category


register = template.Library()

@register.inclusion_tag('news/content.html')
def category_global(Category):
    return {
        'category': Category.objects.all()
            }

# @register.inclusion_tag('news/content.html')