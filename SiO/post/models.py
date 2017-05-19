from django.db import models
from SiO.member.models import Association
from SiO.member.models import Member


# TODO: gjør dette om til to klasser hvor du inndeler5 sender og tekst i to  forskjellige for å forhindre repitisjon.
class Email(models.Model):
    sender = models.CharField(max_length=254)
    sentTime = models.DateTimeField(auto_now_add=True, blank=False)
    subject = models.CharField(max_length=254)
    receiver = models.CharField(max_length=254)
    cc = models.CharField(max_length=254)
    bcc = models.CharField(max_length=254)
    message = models.TextField()
    association = models.ForeignKey(Association)

    class Meta:
        db_table = 'Email'




