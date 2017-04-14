from django.db import models
from SiO.member.models import Association
from SiO.member.models import Member
 # Create your models here.


class Meta:
    db_table = 'email'

# TODO: gjør dette om til to klasser hvor du inndeler5 sender og tekst i to  forskjellige for å forhindre repitisjon.
class Email(models.Model):
    sender = models.CharField(max_length=254)
    sentTime = models.DateTimeField(auto_now_add=True, blank=False)

    receiver = models.CharField(max_length=254)
    sendStatus = models.BooleanField()
    message = models.TextField()
    asocNumber = models.OneToOneField(Association)
