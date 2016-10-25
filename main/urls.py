from django.conf.urls import url, include

from main.views import MainView, AboutView
from office.views import OfficeListView

urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^news/', include('news.urls')),
    url(r'^contact/$', OfficeListView.as_view(), name='contact'),
]