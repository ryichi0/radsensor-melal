from rest_framework import serializers
from .models import *


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
            'slug',
            'product_images',
        ]

class ProductDownloadsSerializer(serializers.ModelSerializer):
    datasheet = serializers.SerializerMethodField()
    calibration_software = serializers.SerializerMethodField()
    modbus_poll_software = serializers.SerializerMethodField()
    product_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "product_name",
            "product_image",
            "datasheet",
            "calibration_software",
            "modbus_poll_software",
        ]

    def get_product_image(self, obj):
        image = ProductImage.objects.filter(product=obj).first()
        if image and image.image:
            return image.image.url  # فقط مسیر از MEDIA_URL
        return None

    def get_datasheet(self, obj):
        if obj.datasheet:
            return obj.datasheet.url  # فقط مسیر از MEDIA_URL
        return None

    def get_calibration_software(self, obj):
        if obj.calibration_software and obj.calibration_software.software_file:
            return obj.calibration_software.software_file.url
        return None

    def get_modbus_poll_software(self, obj):
        if obj.modbus_software and obj.modbus_software.software_file:
            return obj.modbus_software.software_file.url
        return None
