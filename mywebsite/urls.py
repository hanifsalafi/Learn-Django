
from django.contrib import admin
from django.urls import path, include

from .views import views as home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.index),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
]