from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
# Create your views here.

class HelloAPIView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self,resquest,format=None):
        """Return a list of APIView features."""

        an_apiview=[
        'Uses http methods as functions',
        'It is similar to traditional django view',
        'Gives you the most control over your project',
        'Is mapped manaually to URLs'
        ]
        return Response({'message':'Hello!' , 'an_apiview':an_apiview})

    def post(self , request):
        """Create a hello messsage with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,ok=None):
        """Handles updating an object."""

        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """Only updates fields provided in the request."""

        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """Deletes and object"""

        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""

    def list(self,request):
        """Returns a hello message"""

        a_viewset=[
        'Uses actions (list,create,retreive,ipdate,partial_update',
        'Automatically maps to urls using routers',
        'Provides more functionality with less code'
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})
