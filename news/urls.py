from django.conf.urls import url
from news.views import NewsListView, NewsDetailView, category, tag

urlpatterns = [
    url(r'^category/(?P<slug>\w+)$', category, name='category'),
    url(r'^$', NewsListView.as_view(), name='news'),
    url(r'^(?P<s  lug>[\w-]+)/$', NewsDetailView.as_view()),

  #  url(r'^category/(?P<slug>\d+)$', 'news.views.category'),
   #  url(r'^test/$', CategoryListView.as_view()),
    # выборку будем делать по slug, представление - category
 #   url(r'^(?P<slug>[\w-]+)/$', 'category'),
 #   url(r'^tag/(?P<slug>[\w-]+)/$', 'tag'),  # тут тоже самое
]