from django.views import generic
from office.models import Office

class MainView(generic.TemplateView):
    template_name = 'main/index.html'

class AboutView(generic.TemplateView):
    template_name = 'main/about.html'

class NewsView(generic.TemplateView):
    template_name = 'main/news.html'

class ContactView(generic.TemplateView):
    template_name = 'main/contact.html'

