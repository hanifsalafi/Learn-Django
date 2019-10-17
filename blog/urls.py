from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path('post/(?P<slug>[\w-]+)/$', views.singlePost, name='post'),
    re_path('category/(?P<categoryInput>[\w-]+)/$', views.categoryPost, name='category')
]