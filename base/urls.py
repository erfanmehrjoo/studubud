"""studybud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import home , room , createRoom , updateroom , deleteroom

urlpatterns = [
    path('' , home , name='home'),
    path('room/<str:pk>' , room , name='room'),
    path('create-room/' , createRoom , name='create-room'),
    path('update-room/<str:pk>/' , updateroom , name='update-room'),
    path('delete-room/<str:pk>/' , deleteroom , name='delete-room')
]
