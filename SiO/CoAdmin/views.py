from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Administrator, Association
from django.shortcuts import get_object_or_404
from django.views.generic import DeleteView, UpdateView, CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin



from SiO.CoAdmin.forms import SignUpForm, EditSignUpForm, ChangePasswordForm, InnsideSignUpForm

# TODO: Controller (en del av backend) for registrering av ny CoAdmin


class admin_overview(ListView):
    template_name = 'CoAdmin/admin_overview.html'
    # TODO: Måtte fjerne model slik at foreningene blir filtrert i henhold til nåværende innlogget CoAdmin
    # model = Administrator

    def get_queryset(self):
        # user = self.request.administrator
        # return Member.objects.filter(asoc_name=user)
        # return Member.objects.select_related(association=administrator.association)
        # return Member.objects.filter(association__in=Association.objects.filter(
        #     administrator__in=Administrator.objects.filter(asoc_name=asoc_name)))
        queryset = Administrator.objects.filter(association=self.request.user.association)
        return queryset


class admin_edit(SuccessMessageMixin, UpdateView):
    model = Administrator
    form_class = EditSignUpForm
    success_url = reverse_lazy('admin_overview')
    template_name = 'CoAdmin/admin_edit.html'
    success_message = 'Admin successful edited'


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
    success_message = 'Admin successful deleted'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(admin_delete, self).delete(request, *args, **kwargs)


def signup(request):
    # if id is not None:
    #     asoc_name = get_object_or_404(Association, id=id)
    # else:
    #     complaint = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # if form.is_valid():
        if not form.is_valid():
            return render(request, 'CoAdmin/signup.html',
                          {'form': form})

        else:
            # form_save = form.save(commit=False)
            # first = form_save.first_name
            # last = form_save.last_name
            # uname = form_save.username
            # mail = form_save.email
            # passw = form_save.password
            # union = form_save.union_position
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            asoc_pk = form.cleaned_data.get('association')
            asoc = Association.objects.get(id=asoc_pk.pk)
            # asoc_name = form.cleaned_data.get('asoc_name')
            # asoc_name = Association.asoc_name
            union_position = form.cleaned_data.get('union_position')
            # form_save.save(force_insert=True)
            # ci = get_object_or_404(Association, asoc_name=form_save.asoc_name)
            Administrator.objects.create_user(username=username, password=password, email=email,
                                              first_name=first_name, last_name=last_name,
                                              association=asoc, union_position=union_position
                                              )
            user = authenticate(username=username, password=password, email=email,
                                first_name=first_name, last_name=last_name,
                                association=asoc, union_position=union_position)
            # messages.add_message(request, messages.SUCCESS,
            #                      'Admin successfully added.')
            # login(request, user) TODO:Denne linjen logger inn ny member øyeblikkelig etter registrering
            return redirect('/')

    else:
        return render(request, 'CoAdmin/signup.html',
                      {'form': SignUpForm()})


def InnsideSignUp(request):
    # if id is not None:
    #     asoc_name = get_object_or_404(Association, id=id)
    # else:
    #     complaint = None
    if request.method == 'POST':
        form = InnsideSignUpForm(request.user, request.POST)
        # if form.is_valid():
        if not form.is_valid():
            return render(request, 'CoAdmin/InnsideSignup.html',
                          {'form': form})

        else:
            # form_save = form.save(commit=False)
            # first = form_save.first_name
            # last = form_save.last_name
            # uname = form_save.username
            # mail = form_save.email
            # passw = form_save.password
            # union = form_save.union_position
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            asoc_pk = form.cleaned_data.get('association')
            asoc = Association.objects.get(id=asoc_pk.pk)
            # asoc_name = form.cleaned_data.get('asoc_name')
            # asoc_name = Association.asoc_name
            union_position = form.cleaned_data.get('union_position')
            # form_save.save(force_insert=True)
            # ci = get_object_or_404(Association, asoc_name=form_save.asoc_name)
            Administrator.objects.create_user(username=username, password=password, email=email,
                                              first_name=first_name, last_name=last_name,
                                              association=asoc, union_position=union_position
                                              )
            user = authenticate(username=username, password=password, email=email,
                                first_name=first_name, last_name=last_name,
                                association=asoc, union_position=union_position)
            messages.add_message(request, messages.SUCCESS,
                                 'Admin successfully added.')
            # login(request, user) TODO:Denne linjen logger inn ny member øyeblikkelig etter registrering
            return redirect('/')

    else:
        return render(request, 'CoAdmin/InnsideSignup.html',
                      {'form': InnsideSignUpForm(request.user)})



