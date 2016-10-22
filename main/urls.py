from django.conf.urls import url

from main.views import MainView, AboutView, NewsView

urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^news/$', NewsView.as_view(), name='news'),
]