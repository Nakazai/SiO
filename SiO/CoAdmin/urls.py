from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^InnsideSignUp/$', views.InnsideSignUp, name='InnsideSignUp'),
    url(r'^admin_overview/$', views.admin_overview.as_view(), name='admin_overview'),
    url(r'^admin_edit/(?P<pk>\d+)$', views.admin_edit.as_view(), name='admin_edit'),
    url(r'^admin_delete/(?P<pk>\d+)$', views.admin_delete.as_view(), name='admin_delete'),
    url(r'^password/$', views.ChangePassword, name='password'),
]

