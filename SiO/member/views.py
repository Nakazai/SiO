from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator

from .models import Member, Association
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, ListView
from django.contrib import messages
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
import time
import datetime

from SiO.member.forms import EditRegForm, RegAsoc, RegForm


class member_overview(ListView):
    template_name = 'member/member_overview.html'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            queryset = Member.objects.filter(association=self.request.user.association).filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(email__icontains=query)
            )
            return queryset
        else:
            queryset = Member.objects.filter(association=self.request.user.association)
            return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(member_overview, self).dispatch(request, *args, **kwargs)


class member_edit(SuccessMessageMixin, UpdateView):
    model = Member
    form_class = EditRegForm
    success_url = reverse_lazy('member_overview')
    template_name = 'member/member_edit.html'
    success_message = 'Member successfully edited'

    def get_queryset(self):
            queryset = Member.objects.filter(association=self.request.user.association)
            return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(member_edit, self).dispatch(request, *args, **kwargs)


class member_delete(SuccessMessageMixin, DeleteView):
    model = Member
    success_url = reverse_lazy('member_overview')
    template_name = 'member/member_delete.html'
    success_message = 'Member successfully deleted'

    # This method will show the Delete-message
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(member_delete, self).delete(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Member.objects.filter(association=self.request.user.association)
        return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(member_delete, self).dispatch(request, *args, **kwargs)


i = datetime.datetime.now()


@login_required
def member_signup(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if not form.is_valid():
            return render(request, 'member/member_signup.html',
                          {'form': form})

        else:
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            asoc_pk = Association.objects.filter(asoc_name=request.user.association)
            asoc = Association.objects.get(id=asoc_pk)
            gender = form.cleaned_data.get('gender')
            reg_date = i.strftime('%Y-%m-%d')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            end_date = form.cleaned_data.get('end_date')
            Member.objects.create(first_name=first_name, last_name=last_name, email=email,
                                  gender=gender, association=asoc,
                                  reg_date=reg_date, date_of_birth=date_of_birth, end_date=end_date)
            messages.add_message(request, messages.SUCCESS,
                                 'Member successfully added')
            return redirect('member_overview')

    else:
        return render(request, 'member/member_signup.html',
                      {'form': RegForm()})


def asoc_signup(request):
    if request.method == 'POST':
        form = RegAsoc(request.user, request.POST)
        if not form.is_valid():
            return render(request, 'member/asoc_signup.html',
                          {'form': form})

        else:
            asoc_name = form.cleaned_data.get('asoc_name')
            Association.objects.create(asoc_name=asoc_name)
            return redirect('/')

    else:
        return render(request, 'member/asoc_signup.html',
                      {'form': RegAsoc(request.user)})




