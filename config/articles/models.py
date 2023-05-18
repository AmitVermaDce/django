from typing import Iterable, Optional
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    content = models.TextField()    
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)

def article_pre_save(sender, instance, *args, **kwargs):
    print("pre save")
    print(sender, instance)
    if (instance.slug == None):
        instance.slug = slugify(instance.title)
    print(args, kwargs)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(*args, **kwargs):
    print("post save")
    print(args, kwargs)

post_save.connect(article_post_save, sender=Article)