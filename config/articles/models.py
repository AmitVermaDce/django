from typing import Iterable, Optional
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    content = models.TextField()    
    # auto_now means whenever model is saved current time will be set
    # auto_now_add means whenever model is added this will be set
    timestamp = models.DateTimeField(auto_now_add=True)
    # here timestamp make sense with added
    updated = models.DateTimeField(auto_now=True)
    # publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)