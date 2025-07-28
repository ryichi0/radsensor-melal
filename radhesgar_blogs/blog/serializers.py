from rest_framework import serializers
from .models import BlogPost, Category, BlogImage, BlogSection

class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = ['image', 'caption']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class BlogSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSection
        fields = ['heading', 'content', 'order']

class BlogPostSerializer(serializers.ModelSerializer):
    images = BlogImageSerializer(many=True, read_only=True)
    sections = BlogSectionSerializer(many=True, read_only=True)
    category = CategorySerializer()

    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'content', 'category',
            'images', 'created_at', 'updated_at', 'sections',
        ]
