from django.conf.urls import *
from news import views

urlpatterns = [
    url(r'^$', views.ArchiveView.as_view(), name='news'),

    url(r'^(?P<pk>[0-9]+)$', views.NewsPostDetail.as_view(), name="newsdetail"),

    #url(r'^search/(?P<dd>\w+)/$', views.ArchiveView.as_view(), name="searchnews"),
]