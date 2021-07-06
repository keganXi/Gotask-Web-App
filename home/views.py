from typing import List
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

class Home(ListView):
    queryset = ""
    template_name = "home/index.html"


class SignUp(ListView):
    queryset = ""
    template_name = "home/signup.html"