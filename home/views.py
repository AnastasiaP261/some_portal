from django.shortcuts import render
from django.views.generic import ListView, DetailView
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


class DetailNew(DetailView):
    template_name = 'home/detail.html'
    model = News


class DetailPublication(DetailView):
    template_name = 'home/detail.html'
    model = Publications



