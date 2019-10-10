from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    position = models.IntegerField(null=True)
    category = models.CharField(max_length=255, null=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return "{}. {}".format(self.id, self.title)