from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from news.models import NewsPost

# Create your views here.

def archive(request):
    obs = NewsPost.objects.all()
    for i in obs:
        i.body = i.body[:200]+'...'
    page = request.GET.get('page', 1)

    paginator = Paginator(obs, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return HttpResponse(render(request, "archive.html", {'posts':posts} ))

def newsdetail(request, NewsPost_id):
    obs = NewsPost.objects.filter(id=NewsPost_id)
    return HttpResponse(render(request, "newsdetail.html", {'posts': obs} ))