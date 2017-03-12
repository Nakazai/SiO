import os

from django.conf import settings as django_settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from SiO.CoAdmin.models import Administrator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render

from SiO.core.forms import ChangePasswordForm, ProfileForm

# TODO: Metoder som må til slik at bruker dirigeres til de rette templates


def home(request):
    if request.user.is_authenticated():
        return render(request, 'core/dashboard.html')
    else:
        return render(request, 'core/cover.html')


@login_required
def dashboard(request):
    # if request.method == 'POST':
    return render(request, 'core/dashboard.html', {})


@login_required
def profile(request, username):
    page_user = get_object_or_404(Administrator, username=username)
    return render(request, 'core/profile.html', {
        'page_user': page_user
    })


@login_required
def settings(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.asoc_name = form.cleaned_data.get('asoc_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Your profile was successfully edited.')

    else:
        form = ProfileForm(instance=user, initial={
            'first_name': user.profile.first_name,
            'last_name': user.profile.last_name,
            'asoc_name': user.profile.asoc_name
            })
    return render(request, 'core/settings.html', {'form': form})


# @login_required
# def password(request):
#     user = request.user
#     if request.method == 'POST':
#         form = ChangePasswordForm(request.POST)
#         if form.is_valid():
#             new_password = form.cleaned_data.get('new_password')
#             user.set_password(new_password)
#             user.save()
#             update_session_auth_hash(request, user)
#             messages.add_message(request, messages.SUCCESS,
#                                  'Your password was successfully changed.')
#             return redirect('password')
#
#     else:
#         form = ChangePasswordForm(instance=user)
#
#     return render(request, 'core/password.html', {'form': form})


