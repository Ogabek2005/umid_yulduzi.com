from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import generics, views
from . import serializers
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


class NeedHelpView(generics.ListAPIView):
    queryset = NeedHelp.objects.all()
    serializer_class = serializers.NeedHelpSerializer