from django.shortcuts import render
from django.http import HttpResponse
from news.models import NewsPost

# Create your views here.

def archive(request):
    return HttpResponse(render(request, "archive.html", {'posts':NewsPost.objects.all()} ))
    #posts = NewsPost.objects.all()
    #t = loader.get_template("archive.html")
    #c = Context({ 'posts':posts })
    #return HttpResponse(t.render(c))

def newsdetail(request, NewsPost_id):
    return HttpResponse(render(request, "newsdetail.html", {'posts':NewsPost.objects.filter(id=NewsPost_id)} ))