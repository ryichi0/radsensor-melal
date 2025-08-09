from django.urls import path
from .views import BlogPostExportView, BlogPostDetailView, BlogPostsByCategoryView

app_name = 'blog'

urlpatterns = [
    path('all/', BlogPostExportView.as_view(), name='post-export'),
    path('<int:blog_id>/', BlogPostDetailView.as_view(), name='blog-detail'),
    path('category/<int:category_id>/', BlogPostsByCategoryView.as_view(), name='blogs-by-category'),
]
