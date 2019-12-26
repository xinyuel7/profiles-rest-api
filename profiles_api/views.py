from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers #tell our API view what data to expect when making posts put and patch request
from profiles_api import models
from profiles_api import permissions

#when rest framework call the apiview, return response object
class HelloApiView(APIView): #define the application logic for our endpoint(URL)
    """Test API view"""
    serializer_class = serializers.HelloSerializer
    #add functions for particular HTTP method that you want to support on your endpoint
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',#all the functions that you can addto your API to support the different HTTP request
        'Is similar to a traditional Django View',
        'Gives you the most control over you application logic',
        'Is mapped manually to URLS',
        ]
        return Response({'message':'Hello', 'an_apiview':an_apiview}) #only list or dictionary can be converted to json


    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        #serializer provides the functionality to validate the input

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!' # f function: insert the {name variable} into the string
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, #dictionary of all the errors basedon the validation rules
                status=status.HTTP_400_BAD_REQUEST # by default, we return a 200, change this to a 400 bad request
            )


    def put(self, request, pk=None): #request->new object that should replace the old one
        """Handle updating an object""" # primary key->id of the object
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None): #only update the fields in the request
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    #represent functions that you will perfoem on a typical API
    def list(self, request): #list a set of objects that the viewsets represent
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,) #tuple
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
