import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from SiO.CoAdmin.models import Administrator
from django.shortcuts import get_object_or_404, redirect, render, render_to_response


from SiO.core.forms import ChangePasswordForm, ProfileForm


def home(request):
    if request.user.is_authenticated():
        return render(request, 'core/dashboard.html')
    else:
        return render(request, 'core/cover.html')


@login_required
def dashboard(request):
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





