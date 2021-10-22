from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView
from .models import News, Publications


class Home(ListView):
    template_name = 'home/home_list.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        context['news'] = News.objects.order_by('updated_at').reverse()[:4]
        return context

    def get_queryset(self):
        return Publications.objects.order_by('updated_at').reverse()


class DetailNew(DetailView, UpdateView):
    template_name = 'home/detail.html'
    model = News
    fields = ['likes_num', 'dislikes_num']

    def post(self, request, *args, **kwargs):
        return post(self, request, *args, **kwargs)


class DetailPublication(DetailView, UpdateView):
    template_name = 'home/detail.html'
    model = Publications
    fields = ['likes_num', 'dislikes_num']

    def post(self, request, *args, **kwargs):
        return post(self, request, *args, **kwargs)


def post(cls, request, *args, **kwargs):
    try:
        obj = cls.model.objects.get(pk=kwargs['pk'])

        if request.POST['like_type'] == 'like':
            obj.likes_num += 1
        elif request.POST['like_type'] == 'dislike':
            obj.dislikes_num += 1
        obj.save()
        return redirect('publication', pk=kwargs['pk'])
    except:
        return redirect('home')
