from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ChartView/$', views.ChartView.as_view(), name='ChartView'),
    url(r'^ChartView/month$', views.ChartViewMonth.as_view(), name='ChartView/month'),
    # url(r'^api/data/$', views.get_data, name='api-data'),
    url(r'^api/chart/data/$', views.ChartData.as_view()),
]




