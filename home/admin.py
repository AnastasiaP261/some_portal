from django.contrib import admin
from .models import News, Publications


l_disp = ['pk', 'title', 'content', 'created_at', 'updated_at', 'author', 'likes_num', 'dislikes_num']


class NewsAdmin(admin.ModelAdmin):
    list_display = l_disp


class PublicationsAdmin(admin.ModelAdmin):
    list_display = l_disp


admin.site.register(News, NewsAdmin)
admin.site.register(Publications, PublicationsAdmin)

