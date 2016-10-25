from django.views import generic
from news.models import New

class NewsView(generic.TemplateView):
    template_name = 'news/news.html'