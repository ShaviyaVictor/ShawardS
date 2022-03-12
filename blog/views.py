from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request) :

  return HttpResponse('<h1>Blog Home</h1>')



def collection(request) :

  return HttpResponse('<h1>Blog Collections</h1>')



def talent(request) :

  return HttpResponse('<h1>Blog Talent</h1>')



def blog(request) :

  return HttpResponse('<h1>Blog Page</h1>')



def about(request) :

  return HttpResponse('<h1>Blog About</h1>')



def contact(request) :

  return HttpResponse('<h1>Blog Contact</h1>')



