from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView



urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),

    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

    # path('collection/', PostListView.as_view(), name='blog-collection'),

    path('collection/', views.collection, name='blog-collection'),

    path('talent/', views.talent, name='blog-talent'),
    path('blog/', views.blog, name='blog-blog'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
]