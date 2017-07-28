from django.conf.urls import *
from news.views import archive


urlpatterns = [
    url(r'^$', archive),
]