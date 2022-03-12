from django.shortcuts import render
from django.http import HttpResponse



# Dummy data to portray our home db table
posts = [
  {
    'author': 'Victor Shaviya',
    'title': 'Project 1 Blog',
    'location': 'Nairobi',
    'date_posted': 'March 11, 2022',
    
  },
  {
    'author': 'Josphine Mbaisi',
    'title': 'Project 2 Digi',
    'location': 'Nairobi',
    'date_posted': 'Feb 22, 2021',
    
  },
  {
    'author': 'Norris Ambune',
    'title': 'Project 3 Tennis',
    'location': 'Nairobi',
    'date_posted': 'April 28, 2020',
    
  }
]


# Create your views here.
def home(request) :

  context = {
    'posts': posts,
    'title': 'ShawardS~Home',
  }

  return render(request, 'blog/home.html', context)



def collection(request) :

  context = {
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



