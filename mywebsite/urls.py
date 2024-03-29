
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView, RedirectView
from .views import views as home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', RedirectView.as_view(pattern_name="index"), name='home'),
    path('', home.index, name="index"),
    path('about/', include(('about.urls', 'about'), namespace='about')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    re_path('^(?P<name>[\w|\W]+)/(?P<date>0?[1-9]|1[0-9]|2[0-9]|3[0-1])/(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', home.test, name='test')
]