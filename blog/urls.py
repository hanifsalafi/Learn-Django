from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/create/', views.create_post, name='create-post'),
    re_path('post/(?P<slug>[\w-]+)/$', views.singlePost, name='post'),
    re_path('category/(?P<categoryInput>[\w-]+)/$', views.categoryPost, name='category')
]