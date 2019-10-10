from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    
    def __str__(self):
        return "{}. {}".format(self.id, self.title)