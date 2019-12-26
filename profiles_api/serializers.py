from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10) #whenever sending a post or patch request, expect an input with name with maximum length of 10
