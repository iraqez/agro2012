from django.conf.urls import url
from news.views import NewsListView, NewsDetailView, category, tag

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news'),
    url(r'^(?P<slug>[\w-]+)/$', NewsDetailView.as_view()),
]