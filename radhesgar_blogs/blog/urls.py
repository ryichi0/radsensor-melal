from django.urls import path
from .views import BlogPostList, BlogPostDetail, CategoryList

urlpatterns = [
    path('posts/', BlogPostList.as_view(), name='post-list'),
    path('posts/<slug:slug>/', BlogPostDetail.as_view(), name='post-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
]
