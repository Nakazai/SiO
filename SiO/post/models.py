from django.db import models
from SiO.member.models import Association
from SiO.member.models import Member
# Create your models here.
from SiO.member.models import Association
1import datetime
import re

class Meta:
    db_table = 'email'


class Email(models.Model):
    sender = models.CharField(max_length=254)
    sentTime = models.DateTimeField(auto_now_add=True, blank=False)

    receiver = models.CharField(max_length=254)
    sendStatus = models.BooleanField()
    message = models.TextField()
    asocNumber = models.ForeignKey(Association)
