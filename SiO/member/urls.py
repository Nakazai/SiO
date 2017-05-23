from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^member_overview/$', views.member_overview.as_view(), name='member_overview'),
    url(r'^member_signup/$', views.member_signup, name='member_signup'),
    url(r'^asoc_signup/$', views.asoc_signup, name='asoc_signup'),
    url(r'^member_edit/(?P<pk>\d+)$', views.member_edit.as_view(), name='member_edit'),
    url(r'^member_delete/(?P<pk>\d+)$', views.member_delete.as_view(), name='member_delete'),
    url(r'^django_popup_view_field/', include('django_popup_view_field.urls')),

]
