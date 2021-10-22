from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView
from .models import *


class Home(ListView):
    template_name = 'home/home_list.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        context['news'] = News.objects.order_by('created_at').reverse()[:4]
        return context

    def get_queryset(self):
        return Publications.objects.order_by('created_at').reverse()


class DetailNew(DetailView, UpdateView):
    template_name = 'home/detail.html'
    model = News
    fields = ['likes_num', 'dislikes_num']

    def get_context_data(self, **kwargs):
        context = super(DetailNew, self).get_context_data(**kwargs)

        res = LikesNews.objects.filter(id_user=self.request.user.id, id_posts=self.kwargs['pk'])
        context['button_visible'] = False if len(res) else True

        return context

    def post(self, request, *args, **kwargs):
        try:
            kwargs['addit_table'] = LikesNews
            pk = edit(self, request, *args, **kwargs)
            return redirect('new', pk=pk)
        except:
            return redirect('home')


class DetailPublication(DetailView, UpdateView):
    template_name = 'home/detail.html'
    model = Publications
    fields = ['likes_num', 'dislikes_num']

    def get_context_data(self, **kwargs):
        context = super(DetailPublication, self).get_context_data(**kwargs)

        res = LikesPublications.objects.filter(id_user=self.request.user.id, id_posts=self.kwargs['pk'])
        context['button_visible'] = False if len(res) else True

        return context

    def post(self, request, *args, **kwargs):
        try:
            kwargs['addit_table'] = LikesPublications
            pk = edit(self, request, *args, **kwargs)
            return redirect('publication', pk=pk)
        except:
            return redirect('home')


def edit(cls, request, *args, **kwargs):
    obj = cls.model.objects.get(pk=kwargs['pk'])  # объект поста(новости/публикации/комментария)
    addit_table = kwargs['addit_table']  # соответствующая доп таблица для связи с пользователем
    usr_pk = request.user.id  # ид юзера

    # проверка, оценивал ли уже юзер этот пост
    user_likes = addit_table.objects.filter(id_user=usr_pk, id_posts=kwargs['pk'])
    if len(user_likes) == 0:
        like_type = request.POST['like_type']  # тип оценки(лайк/дизлайк)
        if like_type == 'like':
            obj.likes_num += 1
        elif like_type == 'dislike':
            obj.dislikes_num += 1
        obj.save()

        addit_table.objects.create(id_user=User.objects.get(pk=usr_pk),
                                   id_posts=obj,
                                   like=(True if like_type == 'like' else False))
    return kwargs['pk']
