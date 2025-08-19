from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product
from .serializers import ProductDetailSerializer, ProductSerializer, ProductDownloadsSerializer
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


class ProductDetailsView(APIView):
    def get(self, request, slug):
        try:
            product = get_object_or_404(Product, slug=slug)
            serializer = ProductDetailSerializer(product, many=False)
            data = json.dumps(serializer.data, indent=2, ensure_ascii=False)
            response = HttpResponse(data, content_type='application/json')
            return response
        except Exception as e:
            print("❌ Error during export:", str(e))
            raise e

class ProductExportView(APIView):
    def get(self, request):
        try:
            product = Product.objects.all()
            serializer = ProductSerializer(product, many=True)
            data = json.dumps(serializer.data, indent=2, ensure_ascii=False)
            response = HttpResponse(data, content_type='application/json')
            return response
        except Exception as e:
            print("❌ Error during export:", str(e))
            raise e


class DownloadExportView(APIView):
    def get(self, request):
        try:
            download_links = Product.objects.all()
            serializer = ProductDownloadsSerializer(download_links, many=True, context={'request': request})
            data = json.dumps(serializer.data, indent=2, ensure_ascii=False)
            response = HttpResponse(data, content_type='application/json')
            return response
        except Exception as e:
            print("❌ Error during export:", str(e))
            raise e

