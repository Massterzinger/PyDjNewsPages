from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic
from news.models import NewsPost

# Create your views here.

'''
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
    return (render(request, "archive.html", {'posts':posts} ))
'''
#def newsdetail(request, NewsPost_id):
#    obs = get_object_or_404(NewsPost, pk=NewsPost_id)
#    return (render(request, "newsdetail.html", {'posts': obs} ))

class ArchiveView(generic.ListView):
    template_name = "archive.html"
    context_object_name = "posts"
    paginate_by = 10
    def get_queryset(self):
        obs = NewsPost.objects.all()
        for i in obs:
            i.body = i.body[:200]+'...'
        return obs
        

class NewsPostDetail(generic.DetailView):
    model = NewsPost
    context_object_name = 'posts'
    template_name='newsdetail.html'