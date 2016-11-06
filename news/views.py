from django.views import generic
from news.models import New, Category

# class NewsView(generic.TemplateView):
#     template_name = 'news/list.html'

# class CategoryListView(generic.TemplateView):
#     template_name = 'news/content.html'
#     category = Category.objects.all()
#     def get_context_data(self, **kwargs):
#         context = super(CategoryListView, self).get_context_data(**kwargs)
#         context["category"] = self.category
#         return context

class NewsListView(generic.ListView):
    model = New
    template_name = 'news/list.html'

    # category = Category.objects.all()
    # def get_context_data(self, **kwargs):
    #     context = super(NewsListView, self).get_context_data(**kwargs)
    #     context["category"] = self.category
    #     return context

class NewsDetailView(generic.DetailView):
    model = New
    template_name = 'news/detail.html'


# class CategoryListView(generic.TemplateView):
# #    template_name = 'news/content.html'
#     category = Category.objects.all()
#     def get_context_data(self, **kwargs):
#         context = super(CategoryListView, self).get_context_data(**kwargs)
#         context["category"] = self.category
#         return context