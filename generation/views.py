from .models import GeneratedString
from .serializers import GeneratedStringSerializer
from rest_framework import generics

# Create your views here.

class GeneratedStringListCreate(generics.ListCreateAPIView):
    queryset = GeneratedString.objects.all()
    serializer_class = GeneratedStringSerializer
