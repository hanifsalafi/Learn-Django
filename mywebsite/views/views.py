from django.shortcuts import render
from django.http import HttpResponse
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

def test(request, name, date, year, month):
    heading = "<h1>Test URL Dinamis</h1>"
    str = heading + "<p>Namaku {}, Lahir Tanggal {}-{}-{}</p>".format(name, date, month, year)
    return HttpResponse(str)