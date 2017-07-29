from django.shortcuts import render
from django.http import HttpResponse
from news.models import NewsPost

# Create your views here.

def facepage(request):
    obs = NewsPost.objects.all()[:3]
    for i in obs:
        i.body = i.body[:86]+'...'
    return HttpResponse(render(request, "face.html", {'posts':obs} ))