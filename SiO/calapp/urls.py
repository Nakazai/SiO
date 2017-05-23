from django.conf.urls import include, url
from django.contrib import admin


from . import views

urlpatterns = [
	url(r'^calendar/event/get/(?P<start>.+)/(?P<end>.+)/', views.event_get),
	url(r'^calendar/event/setsync/', views.event_setsync),
	url(r'^calendar/event/delete/', views.event_delete),
	url(r'^calendar/event/addedit/', views.event_add_edit),
	url(r'^calendar/', views.calendar.as_view(), name='calendar'),

]

