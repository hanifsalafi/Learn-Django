from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Post
# Create your views here.

sub_dir = 'blog/'

def index(request):
    # queryset
    posts = Post.objects.all()
    
    posts_categories = Post.objects.values('category').distinct()

    context = {
        'judul': 'Blog',
        'sub_judul': 'Dashboard',
        'banner': 'blog/img/banner_blog.png',
        'nav': [
            ['index', 'Home'],
            ['about:index', 'About'],
            ['blog:index', 'Blog']
        ],
        'Posts': posts,
        'Categories': posts_categories
    }
    return render(request, sub_dir+'blog.html', context)

def categoryPost(request, categoryInput):
    # queryset
    posts = Post.objects.filter(category=categoryInput)

    posts_categories = Post.objects.values('category').distinct()

    context = {
        'judul': 'Kategori {}'.format(categoryInput.title()),
        'sub_judul': 'Dashboard',
        'banner': 'blog/img/banner_blog.png',
        'nav': [
            ['index', 'Home'],
            ['about:index', 'About'],
            ['blog:index', 'Blog']
        ],
        'Posts': posts,
        'Categories': posts_categories
    }
    return render(request, sub_dir+'blog.html', context)

def singlePost(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'judul': 'Konten Blog',
        'sub_judul': 'Popular Post',
        'banner': 'blog/img/banner_blog.png',
        'nav': [
            ['index', 'Home'],
            ['about:index', 'About'],
            ['blog:index', 'Blog']
        ],
        'post': post
    }
    return render(request, sub_dir+'blog.html', context)


def create_post(request):

    contact_form = ContactForm()

    context = {
        'judul': 'Buat Postingan',
        'sub_judul': 'Create Post',
        'banner': 'blog/img/banner_blog.png',
        'nav': [
            ['index', 'Home'],
            ['about:index', 'About'],
            ['blog:index', 'Blog']
        ],
        'form': contact_form
    }

    print(request.POST)

    return render(request, sub_dir+'create_post.html', context)
