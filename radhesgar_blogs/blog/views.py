from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import BlogPost, Category
from .serializers import BlogPostSerializer, BlogPostDetailSerializer, BlogPostsByCategorySerializer
from rest_framework.views import APIView
import json
from django.http import HttpResponse


class BlogPostExportView(APIView):
    def get(self, request, *args, **kwargs):
        posts = BlogPost.objects.all().order_by('-created_at')
        serializer = BlogPostSerializer(posts, many=True)
        data = json.dumps(serializer.data, indent=2, ensure_ascii=False)
        response = HttpResponse(data, content_type='application/json')
        return response

class BlogPostDetailView(RetrieveAPIView):
    def get(self, request, blog_id):
        try:
            blog = BlogPost.objects.get(pk=blog_id)
        except Category.DoesNotExist:
            return HttpResponse(json.dumps({'error': 'Category not found'}, ensure_ascii=False), status=404, content_type='application/json')
        serializer = BlogPostDetailSerializer(blog, many=False)
        data = json.dumps(serializer.data, indent=2, ensure_ascii=False)
        return HttpResponse(data, content_type='application/json')


class BlogPostsByCategoryView(APIView):
    def get(self, request, category_id, *args, **kwargs):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return HttpResponse(json.dumps({'error': 'Category not found'}, ensure_ascii=False), status=404, content_type='application/json')

        queryset = BlogPost.objects.filter(category=category)
        serializer = BlogPostsByCategorySerializer(queryset, many=True)
        data = json.dumps(serializer.data, indent=2, ensure_ascii=False)
        return HttpResponse(data, content_type='application/json')

