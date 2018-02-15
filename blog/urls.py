from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^series/(?P<series_id>[0-9a-zA-Z_\-]+)/$', views.series, name='series'),
    url(r'^search/$', views.search, name='search'),
    url(r'^about/$', views.test, name='about'),
]
