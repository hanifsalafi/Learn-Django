from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul': 'Website Tekno',
        'sub_judul': 'Blog Hanif',
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog', 'Blog']
        ],
        'banner': 'img/banner_home.png'
    }
    return render(request, 'index.html', context)