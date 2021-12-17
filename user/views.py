from rest_framework import generics
from rest_framework.settings import api_settings 
from rest_framework.authtoken.views import  ObtainAuthToken
from user import serializers
from user.serializers import UserSerializer, AuthTokenSerializer 

class CreateUserView(generics.CreateAPIView):

    serializer_class=UserSerializer

class CreateTokenView(ObtainAuthToken):
    '''new token'''

    serializer_class=AuthTokenSerializer
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES



 
