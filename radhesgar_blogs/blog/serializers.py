from rest_framework import serializers
from .models import BlogPost, Category, BlogSection, ListItems


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ListItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItems
        fields = ['item']

class BlogSectionSerializer(serializers.ModelSerializer):
    list_items = ListItemsSerializer(many=True, read_only=True)
    class Meta:
        model = BlogSection
        fields = ['heading', 'content', 'order', 'image', 'list_items', ]

class BlogPostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = BlogPost
        fields = [
            'id', 'title','content', 'category', 'image',
        ]

class BlogPostDetailSerializer(serializers.ModelSerializer):
    sections = BlogSectionSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'content', 'category',
            'image', 'sections'
        ]

class BlogPostsByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'content',
            'image'
        ]