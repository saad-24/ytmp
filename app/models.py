from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Logo(models.Model):
    image_url = models.URLField(max_length=200) 


class Trending(models.Model):
    image_url = models.URLField(max_length=200)
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)


class Horizontal_Adsense(models.Model):
    image_url = models.URLField(max_length=200)


class Vertical_Adsense(models.Model):
    image_url = models.URLField(max_length=200)


class Blogs(models.Model):
    blog_name = models.CharField(max_length=200)
    blog_text = RichTextField()
    blog_image = models.URLField(max_length=200)

class Privacy(models.Model):
    privacy_text = RichTextField()

class Terms(models.Model):
    terms_text = RichTextField()