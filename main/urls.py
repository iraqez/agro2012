from django.conf.urls import url

from main.views import MainView, AboutView, NewsView, ContactView
from office.views import OfficeListView

urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^news/$', NewsView.as_view(), name='news'),
    url(r'^contact/$', OfficeListView.as_view(), name='contact'),
]