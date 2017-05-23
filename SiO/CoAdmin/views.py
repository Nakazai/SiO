from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator

from .models import Administrator
from django.views.generic import DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from SiO.member.models import Association


from SiO.CoAdmin.forms import SignUpForm, EditSignUpForm, ChangePasswordForm, InnsideSignUpForm


class admin_overview(ListView):
    template_name = 'CoAdmin/admin_overview.html'

    def get_queryset(self):
        queryset = Administrator.objects.filter(association=self.request.user.association)
        return queryset

# TODO: When session logsout the user it will not give an error of annonymoususer, thx to this function
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(admin_overview, self).dispatch(request, *args, **kwargs)


class admin_edit(SuccessMessageMixin, UpdateView):
    model = Administrator
    form_class = EditSignUpForm
    success_url = reverse_lazy('admin_overview')
    template_name = 'CoAdmin/admin_edit.html'
    success_message = 'Admin successful edited'

    def get_queryset(self):
        queryset = Administrator.objects.filter(association=self.request.user.association)
        return queryset


# @login_required
def ChangePassword(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 'Your password was successfully changed.')
            return redirect('password')

    else:
        form = ChangePasswordForm(instance=user)

    return render(request, 'CoAdmin/password.html', {'form': form})


class admin_delete(DeleteView):
    model = Administrator
    success_url = reverse_lazy('admin_overview')
    template_name = 'CoAdmin/admin_delete.html'
    success_message = 'Admin successfully deleted'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(admin_delete, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """ This will stop the current user from deleting themself. """
        owner = Administrator.objects.filter(association=self.request.user.association)
        obj = super(admin_delete, self).get_object(owner)
        if obj == self.request.user:
            raise Http404
        return obj


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'CoAdmin/signup.html',
                          {'form': form})

        else:
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            asoc_pk = form.cleaned_data.get('association')
            asoc = Association.objects.get(id=asoc_pk.pk)
            union_position = form.cleaned_data.get('union_position')
            Administrator.objects.create_user(username=username, password=password, email=email,
                                              first_name=first_name, last_name=last_name,
                                              association=asoc, union_position=union_position
                                              )
            user = authenticate(username=username, password=password, email=email,
                                first_name=first_name, last_name=last_name,
                                association=asoc, union_position=union_position)
            return redirect('/')

    else:
        return render(request, 'CoAdmin/signup.html',
                      {'form': SignUpForm()})


def InnsideSignUp(request):
    if request.method == 'POST':
        form = InnsideSignUpForm(request.user, request.POST)
        if not form.is_valid():
            return render(request, 'CoAdmin/InnsideSignup.html',
                          {'form': form})

        else:
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            asoc_pk = Association.objects.filter(asoc_name=request.user.association)
            asoc = Association.objects.get(id=asoc_pk)
            union_position = form.cleaned_data.get('union_position')
            Administrator.objects.create_user(username=username, password=password, email=email,
                                              first_name=first_name, last_name=last_name,
                                              association=asoc, union_position=union_position
                                              )
            user = authenticate(username=username, password=password, email=email,
                                first_name=first_name, last_name=last_name,
                                association=asoc, union_position=union_position)
            messages.add_message(request, messages.SUCCESS,
                                 'Admin successfully added.')
            return redirect('admin_overview')

    else:
        return render(request, 'CoAdmin/InnsideSignup.html',
                      {'form': InnsideSignUpForm(request.user)})



