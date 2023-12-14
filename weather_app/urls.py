"""
URL configuration for weather_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from weather_app1.views import forecast
from weather_app1.views import login
from weather_app1.views import about

urlpatterns = [
    path('', forecast, name='forecast'),
    path('about/', about, name='about'),  # Update the URL and name
    path('login/', login, name='login') # Update the URL and name
]
