from django.forms import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """serializer for tag obj"""

    class Meta:
        model=Tag
        fields= ('id','name')
        read_only_fields=('id',)
        
