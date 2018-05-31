from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloAPIView(APIView):
    """Test API View."""

    def get(self,resquest,format=None):
        """Return a list of APIView features."""

        an_apiview=[
        'Uses http methods as functions',
        'It is similar to traditional django view',
        'Gives you the most control over your project',
        'Is mapped manaually to URLs'
        ]
        return Response({'message':'Hello!' , 'an_apiview':an_apiview})
