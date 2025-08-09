from rest_framework.views import APIView
from .models import Product
from .serializers import ProductDetailSerializer, ProductSerializer
import json
from django.http import HttpResponse


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
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