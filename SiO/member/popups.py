from string import ascii_uppercase

from django import forms
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView

from django_popup_view_field.registry import registry_popup_view


class GenderPopupView(TemplateView):
    template_name = "member/popup_gender.html"

registry_popup_view.register(GenderPopupView)



