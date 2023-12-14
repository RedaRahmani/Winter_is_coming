# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.forecast, name='forecast'),
    path('about/', views.about, name='about'),  # Update the URL and name
    path('login/', views.login, name='login') # Update the URL and name
]
