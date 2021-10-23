from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=30)
    likes_num = models.IntegerField(default=0)
    dislikes_num = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('new', kwargs={'pk': self.pk})


class Publications(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=30)
    likes_num = models.IntegerField(default=0)
    dislikes_num = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('publication', kwargs={'pk': self.pk})


# комментарии для новостей
class CommentNews(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    id_post = models.ForeignKey(News, on_delete=models.PROTECT)
    likes_num = models.IntegerField(default=0)
    dislikes_num = models.IntegerField(default=0)
    text = models.TextField(blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


# комментарии для публикаций
class CommentPublication(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)
    id_post = models.ForeignKey(Publications, on_delete=models.PROTECT)
    likes_num = models.IntegerField(default=0)
    dislikes_num = models.IntegerField(default=0)
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


# дополнительные таблицы, реализующие связь многие ко многим для пользователя и лайков
# лайк для новости
class LikesNews(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)
    id_posts = models.ForeignKey(News, on_delete=models.PROTECT)
    like = models.BooleanField(null=True)


# лайк для публикации
class LikesPublications(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)
    id_posts = models.ForeignKey(Publications, on_delete=models.PROTECT)
    like = models.BooleanField(null=True)


# лайк для комментария под новостью
class LikesCommentNews(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)
    id_posts = models.ForeignKey(CommentNews, on_delete=models.PROTECT)
    like = models.BooleanField(null=True)


# лайк для комментария под публикацией
class LikesCommentPublication(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)
    id_posts = models.ForeignKey(CommentPublication, on_delete=models.PROTECT)
    like = models.BooleanField(null=True)
