from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.utils.decorators import method_decorator
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
# class ChartView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'chart/ChartView.html', {})


# class ChartViewMonth(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'chart/ChartView/month.html', {})


# class ChartData(APIView):
#     def get(self, request, format=None):
#         qs_count = Administrator.objects.filter(association=self.request.user.association).count()
#         qs_count1 = Member.objects.filter(association=self.request.user.association).count()

#         labels = ["Board"]
#         default_items = [qs_count]
#         labels2 = ["Member"]
#         default_items = [qs_count2]

#         data = {
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
# TODO:this one shows example of pie-chart
class ChartHigh(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart/chartViewHigh.html', {})

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ChartHigh, self).dispatch(request, *args, **kwargs)


class ChartHighAM(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart/chartViewHighAM.html', {})

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ChartHighAM, self).dispatch(request, *args, **kwargs)


class ChartHighGender(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart/chartViewHighGender.html', {})

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ChartHighGender, self).dispatch(request, *args, **kwargs)


class ChartHighMonth(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart/chartViewHighMonth.html', {})

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ChartHighMonth, self).dispatch(request, *args, **kwargs)


class ChartHighAge(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart/chartViewHighAge.html', {})

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ChartHighAge, self).dispatch(request, *args, **kwargs)


class ChartData(APIView):
    def get(self, request, format=None):
        today = datetime.date.today()

        # Board & Members
        qs_count = Administrator.objects.filter(association=self.request.user.association).count()
        qs_count2 = Member.objects.filter(association=self.request.user.association).count()
        # qs_count3 = Member.objects.filter(reg_date__year=today.year,
        #                                   reg_date__month=today.month).filter(
        #                                   association=self.request.user.association).count()

        # Months
        qs_count01 = Member.objects.filter(reg_date__year=today.year,
                                           reg_date__month='01').filter(
                                          association=self.request.user.association).count()
        qs_count02 = Member.objects.filter(reg_date__year=today.year,
                                           reg_date__month='02').filter(
                                            association=self.request.user.association).count()
        qs_count03 = Member.objects.filter(reg_date__year=today.year,
                                           reg_date__month='03').filter(
                                            association=self.request.user.association).count()
        qs_count04 = Member.objects.filter(reg_date__year=today.year,
                                           reg_date__month='04').filter(
                                             association=self.request.user.association).count()
        qs_count05 = Member.objects.filter(reg_date__year=today.year,
                                           reg_date__month='05').filter(
                                            association=self.request.user.association).count()
        qs_count06 = Member.objects.filter(reg_date__year=today.year,
                                           reg_date__month='06').filter(
            association=self.request.user.association).count()
        qs_count07 = Member.objects.filter(reg_date__year=today.year,
                                           reg_date__month='07').filter(
            association=self.request.user.association).count()
        qs_count08 = Member.objects.filter(reg_date__year=today.year,
                                           reg_date__month='08').filter(
            association=self.request.user.association).count()
        qs_count09 = Member.objects.filter(reg_date__year=today.year,
                                           reg_date__month='09').filter(
            association=self.request.user.association).count()
        qs_count10 = Member.objects.filter(reg_date__year=today.year,
                                           reg_date__month='10').filter(
            association=self.request.user.association).count()
        qs_count11 = Member.objects.filter(reg_date__year=today.year,
                                           reg_date__month='11').filter(
            association=self.request.user.association).count()
        qs_count12 = Member.objects.filter(reg_date__year=today.year,
                                           reg_date__month='12').filter(
            association=self.request.user.association).count()

        # Age
        qs_count13 = Member.objects.filter(date_of_birth__gte=datetime.date(1996, 1, 1),
                                           date_of_birth__lte=datetime.date(2001, 12, 31)).filter(
                                            association=self.request.user.association).count()
        qs_count14 = Member.objects.filter(date_of_birth__gte=datetime.date(1990, 1, 1),
                                           date_of_birth__lte=datetime.date(1995, 12, 31)).filter(
                                            association=self.request.user.association).count()
        qs_count15 = Member.objects.filter(date_of_birth__gte=datetime.date(1984, 1, 1),
                                           date_of_birth__lte=datetime.date(1989, 12, 31)).filter(
                                            association=self.request.user.association).count()

        #Gender
        # if Member.gender == "Male":
        qs_count4 = Member.objects.filter(gender="Male").filter(
                                          association=self.request.user.association).count()
        qs_count5 = Member.objects.filter(gender="Female").filter(
                                          association=self.request.user.association).count()

        # Board & Members
        labels2 = ["Members"]
        default_items2 = [qs_count2]
        labels = ["Board"]
        default_items = [qs_count]

        # Gender
        labels4 = ["Male"]
        default_items4 = [qs_count4]
        labels5 = ["Female"]
        default_items5 = [qs_count5]

        # Months
        labels01 = ["Jan"]
        default_items01 = [qs_count01]
        labels02 = ["Feb"]
        default_items02 = [qs_count02]
        labels03 = ["Mar"]
        default_items03 = [qs_count03]
        labels04 = ["Apr"]
        default_items04 = [qs_count04]
        labels05 = ["May"]
        default_items05 = [qs_count05]
        labels06 = ["Jun"]
        default_items06 = [qs_count06]
        labels07 = ["Jul"]
        default_items07 = [qs_count07]
        labels08 = ["Aug"]
        default_items08 = [qs_count08]
        labels09 = ["Sep"]
        default_items09 = [qs_count09]
        labels10 = ["Oct"]
        default_items10 = [qs_count10]
        labels11 = ["Nov"]
        default_items11 = [qs_count11]
        labels12 = ["Dec"]
        default_items12 = [qs_count12]

        # Age
        labels13 = ["Age 16-21"]
        default_items13 = [qs_count13]
        labels14 = ["Age 22-27"]
        default_items14 = [qs_count14]
        labels15 = ["Age 28-33"]
        default_items15 = [qs_count15]

        data = {
            # Board & Members
            "labels": labels,
            "default": default_items,
            "labels2": labels2,
            "default2": default_items2,
            # "xAxisTitle": 2017,

            # Gender
            "labels4": labels4,
            "default4": default_items4,
            "labels5": labels5,
            "default5": default_items5,

            # Months
            "labels01": labels01,
            "default01": default_items01,
            "labels02": labels02,
            "default02": default_items02,
            "labels03": labels03,
            "default03": default_items03,
            "labels04": labels04,
            "default04": default_items04,
            "labels05": labels05,
            "default05": default_items05,
            "labels06": labels06,
            "default06": default_items06,
            "labels07": labels07,
            "default07": default_items07,
            "labels08": labels08,
            "default08": default_items08,
            "labels09": labels09,
            "default09": default_items09,
            "labels10": labels10,
            "default10": default_items10,
            "labels11": labels11,
            "default11": default_items11,
            "labels12": labels12,
            "default12": default_items12,

            # Age
            "labels13": labels13,
            "default13": default_items13,
            "labels14": labels14,
            "default14": default_items14,
            "labels15": labels15,
            "default15": default_items15
        }
        return Response(data)

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(ChartData, self).dispatch(request, *args, **kwargs)

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








