from rest_framework import generics
from .models import BlogPost, Category
from .serializers import BlogPostSerializer, CategorySerializer

class BlogPostList(generics.ListAPIView):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer

class BlogPostDetail(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

