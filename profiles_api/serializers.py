from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10) #whenever sending a post or patch request, expect an input with name with maximum length of 10

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password') # either make accessible in our API or use to create new nodels with serializers
        extra_kwargs = { #keyword args
            'password': { #key->field value->custom configuration
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data): #overwrite create so password het hashed
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user( #call create_user
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
