from __future__ import unicode_literals

import hashlib
import os.path
import urllib


from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser
from SiO.member.models import Member

# TODO: Her lages det database modeller Admin, Mail og Events

# TODO: Nedenfor er User modellen django produserer default men endret til Administrator


class Administrator(AbstractUser):
    admin_id = models.AutoField(primary_key=True)
    union_position = models.CharField(max_length=100)
    association = models.CharField(max_length=100)

    class Meta:
        db_table = 'Administrator'


class Mail(models.Model):
    domain = models.AutoField(primary_key=True)
    admin_id = models.OneToOneField(Administrator)
    member_no = models.OneToOneField(Member)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'Mail'


class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    admin_id = models.OneToOneField(Administrator)
    place = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'Events'


@python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(Administrator)
    # first_name = models.CharField(max_length=50, null=True, blank=True)
    # last_name = models.CharField(max_length=50, null=True, blank=True)
    # association = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'Profile'

    def __str__(self):
        return self.user.username

    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username

    def get_association_name(self):
        try:
            if self.user.association:
                return self.user.association
            else:
                return self.user.username
        except:
            return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=Administrator)
post_save.connect(save_user_profile, sender=Administrator)


