from django import template
from news.models import Tag, Category, New # импортируем модели
# экземпляр класса, в котором все наши теги будут зарегистрированы
register = template.Library()
# регистрируем наш тег, который будет выводить шаблон right_sidebar.html
@register.inclusion_tag("news/sidebar_template.html")
def show_sidebar():
    tags = Tag.objects.all() # выбираем все теги
    # выбираем все категории
    categories = Category.objects.all().order_by("name")
    # выбираем все статьи по id - для ссылок и title - для списка
    new_posts = New.objects.values('id','title', 'image', 'posted').order_by("-posted")[:4]
    # возвращаем наши объекты в шаблон
 ##   return {'tags': tags, 'categories': categories, 'new_posts': new_posts}
    return {'tags': tags, 'categories': categories, 'new_posts': new_posts}
