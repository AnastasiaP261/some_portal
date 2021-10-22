from django.contrib import admin
from .models import News, Publications


class NewsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'content', 'created_at', 'updated_at', 'author']


class PublicationsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'content', 'created_at', 'updated_at', 'author', 'likes_num', 'dislikes_num']


admin.site.register(News, NewsAdmin)
admin.site.register(Publications, PublicationsAdmin)

