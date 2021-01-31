from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from product_manager.core.serializers import (UserSerializer,
                                              GroupSerializer,
                                              ProductSerializer)
from product_manager.core.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
