from django.views import generic
from news.models import New, Category, Tag
from django.shortcuts import render

class NewsListView(generic.ListView):
    model = New
    template_name = 'news/list.html'

class NewsDetailView(generic.DetailView):
    model = New
    template_name = 'news/detail.html'

def category(request, slug): # получаем аргумент id
    # делаем выборку выбранной категории
    category = Category.objects.select_related().get(slug=slug)
    # выбираем все статьи по выбранной категории
    news = category.new_set.all()
    # возвращаем выбранную категорию и статьи в шаблон category.html
    return render(request, 'news/category.html', {'news': news, 'category': category})

def tag (request, slug): # тут все тоже самое
    tag = Tag.objects.select_related().get(slug=slug)
    news = tag.post_set.all()
    return render(request, 'tagpage.html', {'news': news, 'tag': tag})