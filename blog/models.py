from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    position = models.IntegerField(null=True)
    category = models.CharField(max_length=20, null=True)
    slug = models.SlugField(blank=True, null=True, editable=False)
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)
   
    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return "{}. {}".format(self.id, self.title)