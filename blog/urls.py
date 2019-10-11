from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('recent/', views.recent),
    path('popular/', views.popular),
    path('berita/', views.berita),
    path('blog/', views.blog),
    re_path('post/(?P<slug>[\w-]+)/$', views.singlePost)
]