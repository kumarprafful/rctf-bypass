from rest_framework import serializers
from .models import GeneratedString

class GeneratedStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedString
        fields = '__all__'
