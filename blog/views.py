from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

sub_dir = 'blog/'

def index(request):
    context = {
        'judul': 'Blog',
        'sub_judul': 'Dashboard',
        'banner': 'blog/img/banner_blog.png'
    }
    return render(request, sub_dir+'blog.html', context)

def recent(request):
    context = {
        'judul': 'Blog',
        'sub_judul': 'Recent Post'
    }
    return render(request, sub_dir+'blog.html', context)

def popular(request):
    context = {
        'judul': 'Blog',
        'sub_judul': 'Popular Post'
    }
    return render(request, sub_dir+'blog.html', context)


    