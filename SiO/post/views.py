from django.views.generic import View
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404
from SiO.post.mail import mailHandler
from SiO.post.models import Email
from datetime import datetime


User = get_user_model()


# @login_required
class post(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'post/post.html', {})

def mail(request):
    if request.method == 'POST':
        form = mailHandler(request.user, request.POST)
        if not form.is_valid():
            return render(request, 'member/member_signup.html',
                           {'form': form})
        else:
            sender = form.cleaned_date.get('sender')
            receiver =  form.cleaned_date.get('receiver')
            body = form.cleaned_date.get('body')
            time = datetime.now()
            asoc_number = 1 # TODO: endre denne til faktisk asoc number
            Email.objects.create(
                                 sender=sender,
                                 receiver=receiver,
                                 message=body,
                                 asocNumber=asoc_number,
                                 sentTime=time
            )





            Member.objects.create(first_name=first_name, last_name=last_name, email=email,
                                  student_status=student_status, association=asoc,
                                  reg_date=reg_date, date_of_birth=date_of_birth, end_date=end_date)
            messages.add_message(request, messages.SUCCESS,
                                 'Member successfully added')

