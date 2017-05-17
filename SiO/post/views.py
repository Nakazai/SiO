from django.views.generic import FormView
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404
from SiO.post.mail import mailHandler
from SiO.post.models import Email
from datetime import datetime
from SiO.CoAdmin.models import Administrator
from django.contrib import messages
from SiO.member.models import Association
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail


User = get_user_model()


# @login_required
class mailPost(FormView):
    success_url = '.'
    form_class = mailHandler
    template_name = 'post/post.html'

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Email Sent!')
        return super(mailPost, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.WARNING,
                             'Email not sent. Please try again.')
        return super(mailPost, self).form_invalid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            # asoc_pk = Association.objects.filter(asoc_name=self.request.user.association)
            # asoc = Association.objects.get(id=asoc_pk)
            # asoc(form.cleaned_data['receiver'],
            #              form.cleaned_data['subject'],
            #              form.cleaned_data['message'])
            # sender = form.cleaned_data.get('sender')
            # sender = Administrator.objects.get(email=self.request.user.email)
            # sender = Administrator.objects.get(email=send)
            sender = "noreply@sioforeninger.no"
            receiver = form.cleaned_data.get('receiver')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            time = datetime.now()
            # # ###asoc_number = 1 # TODO: endre denne til faktisk asoc number
            asoc_pk = Association.objects.filter(asoc_name=self.request.user.association)
            asoc = Association.objects.get(id=asoc_pk)
            # msg = EmailMultiAlternatives(message, sender, [receiver])
            # msg.send()
            Email.objects.create(
                sender=sender,
                receiver=receiver,
                subject=subject,
                message=message,
                # ###asocNumber=asoc_number,
                association=asoc,
                sentTime=time
            )
            # self.form_valid(form)
            # messages.add_message(request, messages.SUCCESS,
            #                      'Email Sent!')
            # msg = EmailMultiAlternatives(message, sender, [receiver])
            # msg.send()
            # response.raise_for_status()
            # send_mail("It works!", "This will get sent through Mailgun",
            #           "Anymail Sender <from@example.com>", ["jamallakbir@gmail.com"])
            # send_mail(message, "This will get sent through Mailgun", sender, [receiver])
            send_mail(subject, message, sender, [receiver])
            return self.form_valid(form)
        else:
            return self.form_invalid(form)























        # if form.is_valid():
        #     sender = form.cleaned_data.get('sender')
        #     receiver = form.cleaned_data.get('receiver')
        #     message = form.cleaned_data.get('body')
        #     time = datetime.now()
        #     # ###asoc_number = 1 # TODO: endre denne til faktisk asoc number
        #     asoc_pk = Association.objects.filter(asoc_name=request.user.association)
        #     asoc = Association.objects.get(id=asoc_pk)
        #     Email.objects.create(
        #         sender=sender,
        #         receiver=receiver,
        #         message=message,
        #         # ###asocNumber=asoc_number,
        #         asocNumber=asoc,
        #         sentTime=time
        #     )
        #     return self.form_valid(form)
        # else:
        #     return self.form_invalid(form)





    # def get(self, request, *args, **kwargs):
    #     return render(request, 'post/post.html', {})
    #
    # def form_valid(self, form):
    #     messages.add_message(self.request, messages.SUCCESS, 'Email Sent!')
    #     return super(mailPost, self).form_valid(form)
    #
    # def form_invalid(self, form):
    #     messages.add_message(self.request, messages.WARNING,
    #                          'Email not sent. Please try again.')
    #     return super(mailPost, self).form_invalid(form)
    #
    # def mail(self, request):
    #     if request.method == 'POST':
    #         form = mailHandler(request.user, request.POST)
    #         if not form.is_valid():
    #             return self.form_invalid({'form': form})
    #             # ###return render(request, 'member/member_signup.html',
    #             #                ###{'form': form})
    #         else:
    #             sender = form.cleaned_data.get('sender')
    #             receiver = form.cleaned_data.get('receiver')
    #             body = form.cleaned_data.get('body')
    #             time = datetime.now()
    #             # ###asoc_number = 1 # TODO: endre denne til faktisk asoc number
    #             asoc_pk = Association.objects.filter(asoc_name=request.user.association)
    #             asoc = Association.objects.get(id=asoc_pk)
    #             Email.objects.create(
    #                                  sender=sender,
    #                                  receiver=receiver,
    #                                  message=body,
    #                                  # ###asocNumber=asoc_number,
    #                                  asocNumber=asoc,
    #                                  sentTime=time
    #             )
    #             return self.form_valid(form)






                # Member.objects.create(first_name=first_name, last_name=last_name, email=email,
            #                       student_status=student_status, association=asoc,
            #                       reg_date=reg_date, date_of_birth=date_of_birth, end_date=end_date)
            # messages.add_message(request, messages.SUCCESS,
            #                      'Member successfully added')

