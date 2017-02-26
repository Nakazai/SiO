from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^member_overview/$', views.member_overview, name='member_overview'),
    url(r'^member_overview/$', views.member_overview.as_view(), name='member_overview'),
    url(r'^member_signup/$', views.member_signup, name='member_signup'),
    # url(r'^member_edit/(?P<member_no>\d+)$', views.member_edit, name='member_edit'),
    url(r'^member_edit/(?P<pk>\d+)$', views.member_edit.as_view(), name='member_edit'),
    # url(r'^member_update/(?P<member_no>\d+)$', views.member_update, name='member_update'),
    # url(r'^UpdateMember/$', views.UpdateMember, name='member_update'),
    # url(r'^member_update/(?P<pk>\d+)$', views.member_update.as_view(), name='member_update'),
    # url(r'^member_delete/(?P<member_no>\d+)/$', views.member_delete, name='member_delete')
    url(r'^member_delete/(?P<pk>\d+)$', views.member_delete.as_view(), name='member_delete')
]
