from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from SiO.member.models import Member, Association
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()


class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart/ChartView.html', {})


# def get_data(request, *args, **kwargs):
#     data = {
#         "Sales": 100,
#         "Customers": 10,
#     }
#     return JsonResponse(data)


class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # usernames = [user.username for user in User.objects.all()]
        qs_count = User.objects.all().count()
        qs_count1 = Member.objects.all().count()
        qs_count2 = Association.objects.all().count()
        labels = ["Board", "Members", "Associations"]
        default_items = [qs_count, qs_count1, qs_count2]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)




