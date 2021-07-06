from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.http import Http404

# django rest framework imports.
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        "sign up": "/auth/api/v1/account/sign-up/"
    }
    return Response('api_urls')


class Home(ListView):
    queryset = ""
    template_name = "home/index.html"


class SignUp(ListView):
    queryset = ""
    template_name = "home/signup.html"


class ForgotPassword(ListView):
    queryset = ""
    template_name = "home/forgot-password.html"