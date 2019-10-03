from django.shortcuts import render

# Create your views here.

sub_dir = 'about/'

def index(request):
    context = {
        'judul': 'About',
        'sub_judul': 'Dashboard',
        'banner': 'about/img/banner_about.png'
    }
    return render(request, sub_dir+'about.html', context)

def contact(request):
    context = {
        'judul': 'About',
        'sub_judul': 'Contact'
    }
    return render(request, sub_dir+'about.html', context)

def address(request):
    context = {
        'judul': 'About',
        'sub_judul': 'Address'
    }
    return render(request, sub_dir+'about.html', context)