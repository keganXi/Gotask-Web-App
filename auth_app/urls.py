"""gotaskweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path 

# rest framework imports.
from rest_framework.urlpatterns import format_suffix_patterns 

# import home view
import auth_app.views as auth_view

urlpatterns = [
    path('api/v1/account/sign-up/', auth_view.SignUpAPI.as_view()),
    path('api/v1/account/sign-in/', auth_view.SignInAPI.as_view()),
    path('api/v1/account/u/<slug:username>/', auth_view.UsersAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)