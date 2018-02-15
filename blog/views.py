from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Series

num_post_per_page = 8

def get_popular():
    popular = sorted(Post.objects.all(), key=lambda x: x.views, reverse=True)[:10]
    return popular

def get_context():
    ctx = {
        'popular': get_popular(),
        'series': Series.objects.all(),
    }
    return ctx

def home(request):
    posts = sorted(Post.objects.all(), key=lambda x: x.timestamp, reverse=True)

    page_no = 1
    try:
        page_no = int(request.GET.get('page', 1))
    except:
        pass

    p = Paginator(posts, num_post_per_page)

    try:
        page = p.page(page_no)
    except:
        page = p.page(1)

    context = get_context()
    context['posts']= page

    return render(request, 'blog/home.html', context=context)

def detail(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    p.views += 1
    p.save()

    ctx = get_context()
    ctx['post'] = p

    return render(request, 'blog/post_detail.html', context=ctx)

def series(request, series_id):
    s = get_object_or_404(Series, url=series_id)

    ctx = get_context()
    ctx['s'] = s

    return render(request, 'blog/series.html', context=ctx)

def test(request):
    ctx = get_context()
    return render(request, 'blog/ask.html', ctx)

def search(request):
    q = request.GET.get('q', ' ')

    p = []
    for post in sorted(Post.objects.all(), key=lambda x: x.timestamp, reverse=True):
        if q in post.title or q in post.content:
            p.append(post)

    ctx = get_context()
    ctx['q'] = q
    ctx['posts'] = p

    print(q, len(p))

    return render(request, 'blog/search.html', ctx)
