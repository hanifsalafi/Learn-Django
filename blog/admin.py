from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug','created_time','updated_time']


admin.site.register(Post, PostAdmin)