from django.contrib import admin
from news.models import NewsPost, NewsPostAdmin


# Register your models here.
admin.site.register(NewsPost, NewsPostAdmin)
