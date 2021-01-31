from django.contrib.auth.models import User, Group
from product_manager.core.models import Product
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Senha'}
    )

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'groups']

    def create(self, validated_data):
        data = validated_data
        data['password'] = make_password(data.get('password'))
        return super(UserSerializer, self).create(validated_data)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'name', 'value', 'description']
