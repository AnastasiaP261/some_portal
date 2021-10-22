from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=30)
    # likes_num = models.IntegerField(default=0)
    # dislikes_num = models.IntegerField(default=0)

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


class Users(models.Model):
    name = models.CharField(max_length=60)


class CommentNews(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.PROTECT)
    id_new = models.ForeignKey(News, on_delete=models.PROTECT)
    likes_num = models.IntegerField(default=0)
    dislikes_num = models.IntegerField(default=0)
    text = models.TextField(blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class CommentPublication(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.PROTECT)
    id_pub = models.ForeignKey(Publications, on_delete=models.PROTECT)
    likes_num = models.IntegerField(default=0)
    dislikes_num = models.IntegerField(default=0)
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


# дополнительные таблицы, реализующие связь многие ко многим для пользователя и лайков
class LikesNews(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.PROTECT)
    id_new = models.ForeignKey(News, on_delete=models.PROTECT)
    like = models.BooleanField(null=True)


class LikesPublications(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.PROTECT)
    id_pub = models.ForeignKey(Publications, on_delete=models.PROTECT)
    like = models.BooleanField(null=True)


class LikesCommentNews(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.PROTECT)
    id_com_new = models.ForeignKey(CommentNews, on_delete=models.PROTECT)
    like = models.BooleanField(null=True)


class LikesCommentPublication(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.PROTECT)
    id_com_pub = models.ForeignKey(CommentPublication, on_delete=models.PROTECT)
    like = models.BooleanField(null=True)


