from django.shortcuts import render
from rest_framework import serializers, status, generics, views, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as custom_filters
from apps.users.models import *

class SignupView(generics.GenericAPIView):
    serializer_class = serializers.SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SignInView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class VerifyView(generics.GenericAPIView):
    serializer_class = serializers.VerifySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class NeedHelpFilter(custom_filters.FilterSet):
    user__first_name = custom_filters.CharFilter(field_name='user__first_name', lookup_expr='icontains')

    class Meta:
        model = NeedHelp
        fields = ['user__first_name']

class NeedHelpView(generics.ListAPIView):
    queryset = NeedHelp.objects.all()
    serializer_class = serializers.NeedHelpSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = NeedHelpFilter
    search_fields = ['user__first_name']
    permission_classes = [AllowAny]



class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request,pk, *args, **kwargs):
        from rest_framework import serializers
        if request.user.type == 'admin':
            return super().get(request, *args, **kwargs)
        elif request.user.id != pk:
            raise serializers.ValidationError({"msg": "Bu yerga kirishing uchun admin yoki shu user bolishing kerak"})
        return super().get(request, *args, **kwargs)