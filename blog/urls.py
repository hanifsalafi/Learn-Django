from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/create/', views.create_post, name='create-post'),
    re_path('post/(?P<slug>[\w-]+)/$', views.singlePost, name='post'),
    re_path('category/(?P<categoryInput>[\w-]+)/$', views.categoryPost, name='category'),
    re_path('(?P<redirectTo>[\w-]+)/delete/(?P<deleteId>[0-9]+)', views.delete_post, name='delete-post'),
    re_path('post/update/(?P<updateId>[0-9]+)', views.update_post, name='update-post')
]