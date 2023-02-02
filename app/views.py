from django.shortcuts import render
from rest_framework import viewsets, generics
from . serializers import UserSerializer, UserListSerializer, UserCreateSerializer
from . models import User
from rest_framework.permissions import AllowAny
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]    
        return super(UserViewSet,self).get_permissions()

    def get_serializer_class(self):
        serializer_map = {
            'create': UserCreateSerializer,
            'list': UserListSerializer,
        }
        return serializer_map.get(self.action, UserSerializer)

    def get_queryset(self):
        return super().get_queryset()

