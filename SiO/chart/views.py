from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from SiO.member.models import Member, Association
# from SiO.CoAdmin.models import Member, Association

from SiO.CoAdmin.models import Administrator
from django.core import serializers
from django.contrib.auth.decorators import login_required

from SiO.CoAdmin.serializers import AdministratorSerializer
from SiO.member.serializers import MemberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import datetime
import json


User = get_user_model()


# @login_required
class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart/ChartView.html', {})


class ChartViewMonth(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart/ChartView/month.html', {})


# ##@login_required
# ##class ChartData(generics.ListAPIView):
# class ChartData(APIView):
#
#     # ####serializer_class = AdministratorSerializer, MemberSerializer
#     # ####authentication_classes = ([])
#     # ### authentication_classes = (authentication.TokenAuthentication,)
#     # ####permission_classes = ([permissions.IsAdminUser])
#
#     # ###@login_required
#     def get(self, request, format=None):
#         today = datetime.date.today()
#         # ## usernames = [user.username for user in User.objects.all()]
#         # ## qs_count = User.objects.all().count()
#         # ## if Administrator.objects.filter(association=self.request.user.association):
#         qs_count = Administrator.objects.filter(association=self.request.user.association).count()
#         # ############## qs_count1 = Member.objects.all().count()
#         qs_count1 = Member.objects.filter(association=self.request.user.association).count()
#         # ############# qs_count2 = Association.objects.all().count()
#         qs_count3 = Member.objects.filter(reg_date__year=today.year,
#                                           reg_date__month=today.month).filter(
#                                           association=self.request.user.association).count()
#         # ###qs_count1 = Member.objects.filter(gender=self.request.user.association).count()
#
#         # ###labels3 = ["Gender"]
#         # ###gender_items = [qs_count1]
#         labels2 = ["January",]
#         month_items2 = [qs_count3]
#         labels = ["Board", "Members"]
#         default_items = [qs_count, qs_count1]
#         data = {
#             # ###"labels3": labels3,
#             # ###"genderDif": gender_items,
#             "labels": labels,
#             "default": default_items,
#             "labels2": labels2,
#             "default2": month_items2,
#         }
#         return Response(data)

# def chart_data_json(request):
#     data = {}
#     params = request.GET
#
#     name = params.get('name', '')
#     if name == 'admin_member':
#         data['chart_data'] = Administrator.objects.filter(association=request.user.association).count()
#
#     return HttpResponse(json.dumps(data), content_type='application/json')

# class ChartData(View):
#     def check_valve_data(self):

class ChartHigh(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart/chartViewHigh.html', {})

class ChartHighAM(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart/chartViewHighAM.html', {})


class ChartHighGender(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart/chartViewHighGender.html', {})


class ChartData(APIView):
    def get(self, request, format=None):
        today = datetime.date.today()
        qs_count = Administrator.objects.filter(association=self.request.user.association).count()
        qs_count2 = Member.objects.filter(association=self.request.user.association).count()
        qs_count3 = Member.objects.filter(reg_date__year=today.year,
                                          reg_date__month=today.month).filter(
                                          association=self.request.user.association).count()
        # if Member.gender == "Male":
        qs_count4 = Member.objects.filter(gender="Male").filter(
                                          association=self.request.user.association).count()
        qs_count5 = Member.objects.filter(gender="Female").filter(
                                          association=self.request.user.association).count()

        labels = ["Members"]
        default_items = [qs_count2]
        labels2 = ["Board"]
        default_items2 = [qs_count]
        labels3 = ["Monthly"]
        default_items3 = [qs_count3]
        labels4 = ["Male"]
        default_items4 = [qs_count4]
        labels5 = ["Female"]
        default_items5 = [qs_count5]

        data = {
            "labels": labels,
            "default": default_items,
            "labels2": labels2,
            "default2": default_items2,
            "labels3": labels3,
            "default3": default_items3,
            "labels4": labels4,
            "default4": default_items4,
            "labels5": labels5,
            "default5": default_items5
        }
        return Response(data)

    # data = {'member_no': []}
        #
        # # ###people = Member.objects.all()
        # people = Member.objects.filter(association=self.request.user.association)
        #
        # for unit in people:
        #     data['member_no'].append(unit.member_no)
        #
        # return data


# def chartViewHigh(self, chartID='chart_ID', chart_type='column', chart_height=500):
#     data = ChartData.check_valve_data(self)
#
#     chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
#     title = {"text": 'Check Member Data'}
#     xAxis = {"title": {"text": 'Member'}, "categories": data['member_no']}
#     yAxis = {"title": {"text": 'Data'}}
#     # ###yAxis = {"title": {"text": 'Data'}, "allowDecimals": 'False'}
#     series = [
#         # ###this is details that appears on each columns when hovered
#         {"name": 'MEMBERS', "data": data['member_no']}
#     ]
#
#     return render_to_response('chart/chartViewHigh.html', {'chartID': chartID, 'chart': chart, 'series': series,
#                                                            'title': title, 'xAxis': xAxis, 'yAxis': yAxis})








