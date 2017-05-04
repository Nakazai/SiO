from django.conf.urls import url
from . import views
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model
from SiO.CoAdmin.models import Administrator
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

urlpatterns = [
    url(r'^post/$', views.post.as_view(), name="post")
]
