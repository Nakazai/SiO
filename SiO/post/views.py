from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from django.contrib.auth import get_user_model
from SiO.post.mail import mailHandler
from SiO.post.models import Email
from datetime import datetime
from django.contrib import messages
from SiO.member.models import Association
from django.core.mail import EmailMultiAlternatives, send_mass_mail
from django.core.mail import send_mail
from django.db.models.functions import Concat
from django.db.models import CharField, Value


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
            # sender = "noreply@sioforeninger.no"
            # sender = Association.objects.get(asoc_name=self.request.user.association)
            # sender = Association.objects.filter(asoc_name=self.request.user.association).annotate(email=Concat('asoc_name', Value('@sioforeninger.no')))
            sender = "{} <noreply@sioforeninger.no>".format(self.request.user.association.asoc_name)
            # mail = "@sioforeninger.no"
            # asoc_mail = Association.objects.filter(asoc_name=self.request.user.association)
            # asoc_mail2 = Association.objects.get(id=asoc_mail)
            # sender = asoc_mail2.__str__(mail)
            receiver = form.cleaned_data.get('receiver')
            cc = form.cleaned_data.get('cc')
            bcc = form.cleaned_data.get('bcc')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            time = datetime.now()
            asoc_pk = Association.objects.filter(asoc_name=self.request.user.association)
            asoc = Association.objects.get(id=asoc_pk)
            # msg = EmailMultiAlternatives(message, sender, [receiver])
            # msg.send()
            Email.objects.create(
                sender=sender,
                receiver=receiver,
                # cc=cc,
                # bcc=bcc,
                subject=subject,
                message=message,
                association=asoc,
                sentTime=time
            )
            if cc and bcc:
                msg = EmailMultiAlternatives(subject, message, sender, [receiver], bcc=[bcc], cc=[cc])
            # msg = EmailMultiAlternatives(subject, message, sender, [receiver])
                msg.send()
            else:
                msg = EmailMultiAlternatives(subject, message, sender, [receiver])
                msg.send()
            # send_mail(subject, message, sender, [receiver], [bcc], [cc])
            # send_mass_mail(subject, message, sender, [receiver])
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(mailPost, self).dispatch(request, *args, **kwargs)




