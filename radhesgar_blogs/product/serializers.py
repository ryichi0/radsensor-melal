from rest_framework import serializers
from .models import Product, ProductImage, ProductFeature, ProductApplication, ProductSpecification


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']

class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = ['feature']

class ProductApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductApplication
        fields = ['application']

class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = ['key', 'value']

class ProductDetailSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    product_features = ProductFeatureSerializer(many=True, read_only=True)
    product_applications = ProductApplicationSerializer(many=True, read_only=True)
    product_specifications = ProductSpecificationSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'page_title',
            'sub_title',
            'product_name',
            'product_images',
            'product_features',
            'product_applications',
            'product_specifications',
        ]

class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'product_name',
            'product_images',
        ]