from django.core.mail import EmailMultiAlternatives
from anymail.message import attach_inline_image_file
from django import forms


#  Bytt ut med variabeldata hentet vra views.
class mailHandler(forms.ModelForm):
    # TODO: gjør om sender til å auto-hente foreningsnavn og sende dette som avsendernavn
    sender = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=254,
        required=True)
    # TODO: endre receiver så den kan ta flere epostadresser, hver av dem maks 254 bokstaver lang
    receiver = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=254,
        required=True)
    # TODO Legg til en "Er du sikker på at du vil sende uten emne"-melding
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=130,  # max length satt til 130 da denne er max length før truncate på gmail og outlook
        required =False)
    body = forms.Textarea(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        max_length=1500,
        required=True)




msg = EmailMultiAlternatives(
    subject="Please activate your account",
    body="Click to activate your account: http://example.com/activate",
    from_email="Andreas Jacobsen andreas@sioforeninger.no",
    to=["New User <user1@example.com>", "account.manager@example.com"],
    reply_to=["Helpdesk <support@example.com>"])

msg.tags = ["studentforening ID her", "hva mailen er om"]
msg.track_clicks = True
msg.send()
