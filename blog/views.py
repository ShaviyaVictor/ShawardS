from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request) :

  return render(request, 'blog/home.html')



def collection(request) :

  return render(request, 'blog/collection.html')



def talent(request) :

  return render(request, 'blog/talent.html')



def blog(request) :

  return render(request, 'blog/blog.html')



def about(request) :

  return render(request, 'blog/about.html')



def contact(request) :

  return render(request, 'blog/contact.html')



