from django.views import generic
from news.models import New, Category

# class NewsView(generic.TemplateView):
#     template_name = 'news/list.html'

class NewsListView(generic.ListView):
    model = New
    template_name = 'news/list.html'

class NewsDetailView(generic.DetailView):
    model = New
    template_name = 'news/detail.html'

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'news/content.html'
    context_object_name = 'category'
    queryset = Category.objects.all()