from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Member
from django.http import HttpResponse
from django.http import QueryDict
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView, ListView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views import generic

import json

from SiO.member.forms import RegForm

# TODO: Controller (en del av backend) for registrering av ny member


# def member_overview(request):
#     member = Member.objects.all()
#     context = {'member': member}
#     return render(request, 'member/member_overview.html', context)

class member_overview(ListView):

    model = Member
    # form_class = RegForm
    template_name = 'member/member_overview.html'

# def member_edit(request, member_no):
#     member = Member.objects.get(member_no=member_no)
#     context = {'member': member}
#     return render(request, 'member/member_edit.html', context)

# class member_edit(CreateView):
#     model = Member
#     template_name = 'member/member_edit.html'
#     fields = '__all__'


# def member_update(request, member_no):
#     member = Member.objects.get(member_no=member_no)
#     member.first_name = request.POST['first_name']
#     member.last_name = request.POST['last_name']
#     member.email = request.POST['email']
#     member.student_status = request.POST['student_status']
#     member.reg_date = request.POST['reg_date']
#     member.gender = request.POST['gender']
#     member.birthday = request.POST['birthday']
#     member.save()
#     return redirect('member_overview')

# def member_edit(request, member_no):
#     member = Member.objects.get(member_no=member_no)
#     form = RegForm(request.POST)
#     if form.is_valid():
#         member.first_name = form.cleaned_data.get('first_name')
#         member.last_name = form.cleaned_data.get('last_name')
#         member.email = form.cleaned_data.get('email')
#         member.student_status = form.cleaned_data.get('student_status')
#         member.reg_date = form.cleaned_data.get('reg_date')
#         member.gender = form.cleaned_data.get('gender')
#         member.birthday = form.cleaned_data.get('birthday')
#         member.save()
#     return redirect('member_edit')
    # messages.add_message(request,
    #                      messages.SUCCESS,
    #                      'Your profile was successfully edited.')
    # else:
    #     messages.add_message(request,
    #                          messages.SUCCESS,
    #                          'Something went wrong.')
    # return render(request, 'member/member_edit.html', {'form': form})
    #
    #     else:
    #         return redirect(request, '/')

# class member_update(UpdateView):
#     model = Member
#     template_name = 'member/member_edit.html'
#     fields = ['first_name', 'last_name', 'email', 'student_status', 'reg_date', 'gender', 'birthday', ]

# def member_edit(request, member_no):
#     member = Member.objects.get(member_no=member_no)
#     if request.method == 'POST':
#         form = RegForm(request.POST or None, instance=member)
#         if form.is_valid():
#             # member.first_name = form.cleaned_data.get('first_name')
#             # member.last_name = form.cleaned_data.get('last_name')
#             # member.email = form.cleaned_data.get('email')
#             # # member.student_status = form.cleaned_data.get('student_status')
#             # member.reg_date = form.cleaned_data.get('reg_date')
#             # # member.gender = form.cleaned_data.get('gender')
#             # # member.birthday = form.cleaned_data.get('birthday')
#             form.save()
#             return redirect('member_overview')
#     form = RegForm(instance=member)
#     return render(request, 'member/member_edit.html', {'form': form, 'member': member})


class member_edit(UpdateView):
    model = Member
    form_class = RegForm
    # pk_url_kwarg = 'member_no'
    success_url = reverse_lazy('member_overview')
    template_name = 'member/member_edit.html'


class member_delete(DeleteView):
    model = Member
    success_url = reverse_lazy('member_overview')
    template_name = 'member/member_delete.html'


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
            student_status = form.cleaned_data.get('student_status')
            reg_date = form.cleaned_data.get('reg_date')
            gender = form.cleaned_data.get('gender')
            birthday = form.cleaned_data.get('birthday')
            Member.objects.create(first_name=first_name, last_name=last_name, email=email,
                                  student_status=student_status, reg_date=reg_date,
                                  gender=gender, birthday=birthday)
            # Member.objects.create(first_name=first_name, last_name=last_name, email=email,
            #                       reg_date=reg_date,)
            # Member.save()
            # user = authenticate(first_name=first_name, last_name=last_name, email=email,
            #                     student_status=student_status, reg_date=reg_date,
            #                     gender=gender, birthday=birthday)
            # login(request, user) TODO:Denne linjen logger inn ny member øyeblikkelig etter registrering
            return redirect('/')

    else:
        return render(request, 'member/member_signup.html',
                      {'form': RegForm()})


# class member_delete(DeleteView):
#     def post(self, request, *args, **kwargs):
#         member = get_object_or_404(id=request.POST['member_no'])
#         member.delete()
#         return HttpResponseRedirect('/')
#
#     def get(self, request, *args, **kwargs):
#         member = Member.objects.get(id=kwargs['member_no'])
#         context = {'member': member}
#         return render_to_response("template.html", context, context_instance=RequestContext(request))


# def member_delete(request, member_no):
#     # member = get_object_or_404(Member, member=member_no)
#     member = Member.objects.get(member_no=member_no)
#     if request.method == "POST":
#         member.delete()
#         messages.success(request, "This has been deleted.")
#         return render(request, 'member/member_overview.html')
#     context = {'member': member}
#     return render(request, 'member/member_delete.html', context)

# def member_delete(request):
#
#     if request.method == 'DELETE':
#
#         member = Member.objects.get((QueryDict(request.body).get('member_no')))
#
#         member.delete()
#
#         response_data = {}
#         response_data['msg'] = 'Member was deleted.'
#
#         return HttpResponse(
#             json.dumps(response_data),
#             content_type="application/json"
#         )
#     else:
#         return HttpResponse(
#             json.dumps({"nothing to see": "this isn't happening"}),
#             content_type="application/json"
#         )

# class member_delete(DeleteView):
#     model = Member
#     success_url = reverse_lazy('member_overview')
#     template_name = 'member/member_delete.html'
    # success_url = 'member/member_overview.html'

    # def get_success_url(self):
    #     return reverse('member_overview')
# def member_delete(request, member_no):
#     member = Member.objects.get(member_no=member_no)
#     # messages.add_message(request,
#     #                      messages.SUCCESS,
#     #                      'Are you sure?')
#     member.delete()
#     return render(request, 'member/member_overview.html')
#     # return redirect('/')
