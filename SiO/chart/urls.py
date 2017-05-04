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
    url(r'^ChartView/$', views.ChartView.as_view(), name='ChartView'),
    url(r'^ChartView/month$', views.ChartViewMonth.as_view(), name='ChartView/month'),
    # url(r'^api/data/$', views.get_data, name='api-data'),
    url(r'^api/chart/data/$', views.ChartData.as_view()),
]




