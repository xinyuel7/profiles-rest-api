from rest_framework.views import APIView
from rest_framework.response import Response
#when rest framework call the apiview, return response object


class HelloApiView(APIView): #define the application logic for our endpoint(URL)
    """Test API view"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',#all the functions that you can addto your API to support the different HTTP request
        'Is similar to a traditional Django View',
        'Gives you the most control over you application logic',
        'Is mapped manually to URLS',
        ]
        return Response({'message':'Hello', 'an_apiview':an_apiview}) #only list or dictionary can be converted to json
