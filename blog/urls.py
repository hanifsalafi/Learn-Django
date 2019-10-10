from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('recent/', views.recent),
    path('popular/', views.popular),
    path('berita/', views.berita),
    path('blog/', views.blog)
]