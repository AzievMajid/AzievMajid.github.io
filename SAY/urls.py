from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from SAY.models import Articel

urlpatterns = [
   url(r'^$', ListView.as_view(queryset=Articel.objects.all().order_by("-date")[:20],
   template_name="posts.html")),   
]