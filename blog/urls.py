from django.urls import path
from . import views
from .views import PostListView



urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('collection/', views.collection, name='blog-collection'),
    path('talent/', views.talent, name='blog-talent'),
    path('blog/', views.blog, name='blog-blog'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
]