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

# import home view
import home.views as home_view

urlpatterns = [
    path('api/v1/', home_view.api_overview, name='api-overview'),
    path('', home_view.Home.as_view(), name='home'),
    path('home/', home_view.DashboardHome.as_view(), name='dashboard-home'),
    path('account/sign-up/', home_view.SignUp.as_view(), name='sign-up'),
    path('account/forgot-password/', home_view.ForgotPassword.as_view(), name='forgot-password'),
]
