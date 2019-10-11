from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

sub_dir = 'blog/'

def index(request):
    # queryset
    posts = Post.objects.all()
    context = {
        'judul': 'Blog',
        'sub_judul': 'Dashboard',
        'banner': 'blog/img/banner_blog.png',
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog', 'Blog']
        ],
        'Posts': posts
    }
    return render(request, sub_dir+'blog.html', context)

def berita(request):
    # queryset
    posts = Post.objects.filter(category='berita')
    context = {
        'judul': 'Blog',
        'sub_judul': 'Dashboard',
        'banner': 'blog/img/banner_blog.png',
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog', 'Blog']
        ],
        'Posts': posts
    }
    return render(request, sub_dir+'blog.html', context)

def blog(request):
    # queryset
    posts = Post.objects.filter(category='blog')
    context = {
        'judul': 'Blog',
        'sub_judul': 'Dashboard',
        'banner': 'blog/img/banner_blog.png',
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog', 'Blog']
        ],
        'Posts': posts
    }
    return render(request, sub_dir+'blog.html', context)

def recent(request):
    context = {
        'judul': 'Blog',
        'sub_judul': 'Recent Post',
        'banner': 'blog/img/banner_blog.png',
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog', 'Blog']
        ],
    }
    return render(request, sub_dir+'blog.html', context)

def popular(request):
    context = {
        'judul': 'Blog',
        'sub_judul': 'Popular Post',
        'banner': 'blog/img/banner_blog.png',
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog', 'Blog']
        ],
    }
    return render(request, sub_dir+'blog.html', context)


def singlePost(request, slug):
    post = Post.objects.get(slug=slug)
    title =  '<h3>{}</h3>'.format(post.title)
    category = '<a href="{}">{}</a>'.format(post.category, post.category) 
    body = '<p>{}</p>'.format(post.body)
    return HttpResponse(title+category+body)