from django.db import models


class News(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=30)
    # id_likes = models.
    # id_dislikes =


class Publications(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=30)
    # id_likes = models.
    # id_dislikes =

