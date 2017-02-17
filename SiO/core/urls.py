from django.conf.urls import url
from . import views

# TODO: Denne URL kommer opprinnelig fra SiO.urls ('SiO.core.urls')

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard')
]
