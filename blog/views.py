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


    