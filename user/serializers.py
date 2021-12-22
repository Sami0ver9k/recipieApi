from django.contrib import auth
from django.contrib.auth import get_user, get_user_model,authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    '''serilize user objs'''

    class Meta:
        model=get_user_model()
        fields=('email','password','name')
        extra_kwargs={'password':{'write_only':True,'min_length':4}}

    def create(self,validated_data):
        '''create nw user '''

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance,validated_data):
        '''updating user'''

        password=validated_data.pop('password',None)
        user=super().update(instance,validated_data)

        if password:
            user.set_password(password)
            user.save()
        
        return user



class AuthTokenSerializer(serializers.Serializer):
      """serializer for auth token"""

      email=serializers.CharField()
      password=serializers.CharField(
          style={'input-type': 'password'},
          trim_whitespace=False
      )

      def validate(self,attrs):
          '''validate user '''

          email=attrs.get('email')
          password=attrs.get('password')

          user= authenticate(
              request=self.context.get('request'),
              username=email,
              password=password
          )

          if not user:
              msg=_('unable to authenticate')
              raise serializers.ValidationError(msg,code='authentication')

          attrs['user']=user
          return attrs