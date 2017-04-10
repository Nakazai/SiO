from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()


# @login_required
class post(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'post/post.html', {})

