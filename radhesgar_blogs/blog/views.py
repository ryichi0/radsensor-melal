from rest_framework import generics
from .models import BlogPost, Category
from .serializers import BlogPostSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
import json
from django.http import HttpResponse

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

class BlogPostExportView(APIView):
    def get(self, request, *args, **kwargs):
        posts = BlogPost.objects.all().order_by('-created_at')
        serializer = BlogPostSerializer(posts, many=True)
        data = json.dumps(serializer.data, indent=2, ensure_ascii=False)
        response = HttpResponse(data, content_type='application/json')
        return response
