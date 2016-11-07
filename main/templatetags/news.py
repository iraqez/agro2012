from django import template
from news.models import Tag, Category, New # импортируем модели
# экземпляр класса, в котором все наши теги будут зарегистрированы
register = template.Library()
# регистрируем наш тег, который будет выводить шаблон right_sidebar.html
@register.inclusion_tag("main/main_news.html")
def show_news():
    new_posts = New.objects.values('id','title', 'image', 'posted', 'content', 'slug').order_by("-posted")[:4]
    return {'new_posts': new_posts}