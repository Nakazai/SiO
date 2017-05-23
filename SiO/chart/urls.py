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

    url(r'^api/chart/data/$', views.ChartData.as_view()),
    url(r'^chartViewHigh/$', views.ChartHigh.as_view(), name='chartViewHigh'),
    url(r'^chartViewHighAM/$', views.ChartHighAM.as_view(), name='chartViewHighAM'),
    url(r'^chartViewHighGender/$', views.ChartHighGender.as_view(), name='chartViewHighGender'),
    url(r'^chartViewHighMonth/$', views.ChartHighMonth.as_view(), name='chartViewHighMonth'),
    url(r'^chartViewHighAge/$', views.ChartHighAge.as_view(), name='chartViewHighAge'),
]
