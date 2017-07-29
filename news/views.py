from django.shortcuts import render
from django.http import HttpResponse
from news.models import NewsPost

# Create your views here.

def archive(request):
    obs = NewsPost.objects.all()
    for i in obs:
        i.body = i.body[:200]+'...'
    return HttpResponse(render(request, "archive.html", {'posts':obs} ))

def newsdetail(request, NewsPost_id):
    obs = NewsPost.objects.filter(id=NewsPost_id)
    return HttpResponse(render(request, "newsdetail.html", {'posts': obs} ))