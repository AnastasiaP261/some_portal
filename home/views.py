from django.shortcuts import render
from django.views.generic import ListView
from .models import News, Publications


class Home(ListView):
    pass


