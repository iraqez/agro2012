from django.conf.urls import url

from main.views import MainView, AboutView

urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^about/$', AboutView.as_view(), name='about'),
]