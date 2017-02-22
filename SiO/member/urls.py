from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^member_overview$', views.member_overview, name='member_overview'),
    url(r'^member_signup/$', views.member_signup, name='member_signup'),
]
