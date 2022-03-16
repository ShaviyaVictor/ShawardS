from dataclasses import fields
from re import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.
# def home function replacement
class PostListView(ListView) :
  model = Post

  # <app>/<model>_<viewtype>.html
  template_name = 'blog/home.html'

  context_object_name = 'posts'

  ordering = ['-date_posted']

  paginate_by = 8



# Creating a user's posts view
class UserPostListView(ListView) :
  model = Post

  # <app>/<model>_<viewtype>.html
  template_name = 'blog/user_posts.html'

  context_object_name = 'posts'

  # ordering = ['-date_posted']

  paginate_by = 8

  def get_queryset(self) :
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')


# def home(request) :

#   context = {
#     'posts': Post.objects.all(),
#     'title': 'ShawardS~Home',
#   }

#   return render(request, 'blog/home.html', context)


# Post Detail View
class PostDetailView(DetailView) :
  model = Post


# Post Create View
class PostCreateView(LoginRequiredMixin, CreateView) :
  model = Post
  fields = [
    'project_name',
    'image'
  ]
  

  def form_valid(self, form) :
    form.instance.author = self.request.user    
    return super().form_valid(form)


# Post Update View
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView) :
  model = Post
  fields = [
    'project_name',
    'image'
  ]
  

  def form_valid(self, form) :
    form.instance.author = self.request.user    
    return super().form_valid(form)


  def test_func(self) :
    post = self.get_object()
    if self.request.user == post.author :
      return True  
    return False


# Post Delete View
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView) :
  model = Post

  success_url = '/'


  def test_func(self) :
    post = self.get_object()
    if self.request.user == post.author :
      return True  
    return False




def collection(request) :

  context = {
    'posts': Post.objects.all(),
    'title': 'ShawardS~Collection',
    'paginate_by': 2,
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



