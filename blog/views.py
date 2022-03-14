from dataclasses import fields
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
class PostListView(ListView) :
  model = Post

  # <app>/<model>_<viewtype>.html
  template_name = 'blog/home.html'

  context_object_name = 'posts'

  ordering = ['-date_posted']



# def home(request) :

#   context = {
#     'posts': Post.objects.all(),
#     'title': 'ShawardS~Home',
#   }

#   return render(request, 'blog/home.html', context)



class PostDetailView(DetailView) :
  model = Post



class PostCreateView(CreateView) :
  model = Post
  fields = [
    'project_name',
    'image'
  ]
  



def collection(request) :

  context = {
    'posts': Post.objects.all(),
    'title': 'ShawardS~Collection',
  }

  return render(request, 'blog/collection.html', context)



def talent(request) :

  context = {
    'title': 'ShawardS~Talent',
  }

  return render(request, 'blog/talent.html', context)



def blog(request) :

  context = {
    'title': 'ShawardS~Blog',
  }

  return render(request, 'blog/blog.html', context)



def about(request) :

  context = {
    'title': 'ShawardS~About',
  }

  return render(request, 'blog/about.html', context)



def contact(request) :

  context = {
    'title': 'ShawardS~Contact',
  }

  return render(request, 'blog/contact.html', context)



