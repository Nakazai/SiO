from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from SiO.member.models import Association


class Administrator(AbstractUser):
    union_position = models.CharField(max_length=100)
    email = models.CharField(max_length=255, blank=True, unique=True)
    association = models.ForeignKey(Association)

    class Meta:
        db_table = 'Administrator'

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username


class Event(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    start = models.DateTimeField(blank=False)
    end = models.DateTimeField(blank=False)
    allday = models.BooleanField()
    description = models.TextField(max_length=200)
    synced = models.BooleanField(default=False)
    gid = models.CharField(default='', max_length=100)
    association = models.ForeignKey(Association)

    class Meta:
        db_table = 'Event'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(Administrator)

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


