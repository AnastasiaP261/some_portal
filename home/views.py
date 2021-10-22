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

    def post(self, request, *args, **kwargs):
        try:
            pk = edit(self, request, *args, **kwargs)
            return redirect('new', pk=pk)
        except:
            return redirect('home')


class DetailPublication(DetailView, UpdateView):
    template_name = 'home/detail.html'
    model = Publications
    fields = ['likes_num', 'dislikes_num']

    def post(self, request, *args, **kwargs):
        try:
            kwargs['addit_table'] = P
            pk = edit(self, request, *args, **kwargs)
            return redirect('publication', pk=pk)
        except:
            return redirect('home')


def edit(cls, request, *args, **kwargs):
    obj = cls.model.objects.get(pk=kwargs['pk'])
    addit_table = kwargs['addit_table']
    usr_pk = request.user.id
    user_likes

    if request.POST['like_type'] == 'like':
        obj.likes_num += 1
    elif request.POST['like_type'] == 'dislike':
        obj.dislikes_num += 1
    obj.save()
    return kwargs['pk']
