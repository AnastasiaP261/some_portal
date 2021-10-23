from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('new/<int:pk>/', DetailNew.as_view(), name='new'),
    path('publication/<int:pk>/', DetailPublication.as_view(), name='publication'),
]