from django.conf.urls import *
from news.views import archive, newsdetail


urlpatterns = [
    url(r'^$', archive, name="news"),

    url(r'^(?P<NewsPost_id>[0-9]+)$', newsdetail, name="newsdetail"),
]