from django.contrib import admin
from .models import *


post_list_display = ['pk', 'title', 'content', 'created_at', 'updated_at', 'author', 'likes_num', 'dislikes_num']
comment_list_display = ['pk', 'id_user', 'id_post', 'likes_num', 'dislikes_num', 'text', 'created_at']


class NewsAdmin(admin.ModelAdmin):
    list_display = post_list_display


class PublicationsAdmin(admin.ModelAdmin):
    list_display = post_list_display


admin.site.register(News, NewsAdmin)
admin.site.register(Publications, PublicationsAdmin)


class CommentNewsAdmin(admin.ModelAdmin):
    list_display = comment_list_display


class CommentPublicationAdmin(admin.ModelAdmin):
    list_display = comment_list_display


admin.site.register(CommentNews, CommentNewsAdmin)
admin.site.register(CommentPublication, CommentPublicationAdmin)
