from rest_framework import mixins, viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated

from core.models import Tag 
from recipe import serializers

class TagViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    '''manage tags in db'''


    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    queryset=Tag.objects.all()
    serializer_class=serializers.TagSerializer

    def get_queryset(self):
        '''return objs for auth users'''

        return self.queryset.filter(user=self.request.user).order_by('-name')

