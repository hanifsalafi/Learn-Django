from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

def validate_title(value):
    title_input = value
    if 'Kampret' in title_input:
        raise ValidationError("Tidak boleh mengandung kata kasar")

def validate_body(value):
    body_input = value
    if 'Jancuk' in body_input:
        raise ValidationError("Tidak boleh mengandung kata cacian")

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, validators=[validate_title])
    body = models.TextField(validators=[validate_body])
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