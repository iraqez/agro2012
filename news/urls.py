from django.conf.urls import url
from news.views import NewsListView, NewsDetailView

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news'),
  #  url(r'^$', CategoryListView.as_view(), name='news'),
   url(r'^(?P<slug>[\w-]+)/$', NewsDetailView.as_view()),
   #  url(r'^test/$', CategoryListView.as_view()),
    # выборку будем делать по slug, представление - category
 #   url(r'^category/(?P<slug>[\w-]+)/$', 'category'),
 #   url(r'^tag/(?P<slug>[\w-]+)/$', 'tag'),  # тут тоже самое
]