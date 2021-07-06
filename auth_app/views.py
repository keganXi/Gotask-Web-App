from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import Http404, response
from django.contrib.auth import login, logout, authenticate

# django rest framework.
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

# serializers.
from auth_app.serializers import UserAccountSerializer, SignInSerializer

# Create your views here.

class UsersAPI(APIView):

    def handler(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404 

    def get(self, request, username, format=None):
        user = self.handler(username)
        serializer = UserAccountSerializer(user)
        return Response(serializer.data)


class SignUpAPI(APIView):

    def post(self, request, format=None):
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            if not User.objects.filter(email=request.data.get('email')).exists():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SignInAPI(APIView):

    def get_object(self, email):
        try:
            user = User.objects.get(email=email)
            return user.username
        except User.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            # authenticate user.
            get_user = self.get_object(serializer.data['email'])
            auth_user = authenticate(request, username=get_user, password=serializer.data['password'])
            # check if user exists.
            if auth_user is not None:
                # login user.
                login(request, auth_user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



