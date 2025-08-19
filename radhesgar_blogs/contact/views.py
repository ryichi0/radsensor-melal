from rest_framework.views import APIView
from .models import ContactMessage
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactMessageSerializer

class ContactMessageCreateView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Contact saved successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
