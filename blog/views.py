from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm
from .models import Post
from django.utils.text import slugify
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

    post_form = PostForm(request.POST or None)
    errors = None

    if request.method == 'POST':
        if post_form.is_valid():
            # Post.objects.create(
            #     title = post_form.cleaned_data.get('title'),
            #     category = post_form.cleaned_data.get('category'),
            #     body = post_form.cleaned_data.get('body')
            # )
            post_form.save()
            return redirect('blog:index')
        else:
            list_error = []
            for field, errors in post_form.errors.items():
                error_str = '{} - {}'.format(field.capitalize(), ','.join(errors))
                list_error.append(error_str)
            errors = list_error 

    context = {
        'judul': 'Buat Postingan',
        'sub_judul': 'Create Post',
        'banner': 'blog/img/banner_blog.png',
        'nav': [
            ['index', 'Home'],
            ['about:index', 'About'],
            ['blog:index', 'Blog']
        ],
        'form': post_form,
        'errors': errors
    }

    return render(request, sub_dir+'create_post.html', context)


def delete_post(request, redirectTo, deleteId):
    Post.objects.filter(id=deleteId).delete()
    posts = Post.objects.filter(category=redirectTo)
    if posts.count() == 0:
        return redirect('blog:index')
    else:
        return redirect('blog:category', categoryInput=redirectTo)
    

def update_post(request, updateId):
    post_update = Post.objects.get(id=updateId)

    data = {
        'title' : post_update.title,
        'category' : post_update.category,
        'body' : post_update.body
    }
    form_update = PostForm(request.POST or None, initial=data, instance=post_update)
    errors = None
    if request.method == 'POST':
        if form_update.is_valid():
            form_update.save()
            return redirect('blog:index')
        else:
            list_error = []
            for field, errors in form_update.errors.items():
                error_str = '{} - {}'.format(field.capitalize(), ','.join(errors))
                list_error.append(error_str)
            errors = list_error 

    context = {
        'judul': 'Edit Postingan',
        'sub_judul': 'Edit Post',
        'banner': 'blog/img/banner_blog.png',
        'nav': [
            ['index', 'Home'],
            ['about:index', 'About'],
            ['blog:index', 'Blog']
        ],
        'form': form_update,
        'errors': errors
    }

    return render(request, sub_dir+'create_post.html', context)
    