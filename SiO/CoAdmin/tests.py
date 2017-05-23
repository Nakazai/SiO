from django.test import Client
from django.test import TestCase
from SiO.CoAdmin.models import Event, Association, Administrator, Profile
from django.utils import timezone
from django.core.urlresolvers import reverse


class EventTest(TestCase):
    def setUp(self):
        self.asoc = Association.objects.create(id=1)
        self.event = Event.objects.create(name="LAN",
                                          start=timezone.now(),
                                          end=timezone.now(),
                                          allday=False,
                                          synced=True,
                                          association=self.asoc)
        self.c = Client()

    def test_event_creation(self):
        w = self.event
        self.assertTrue(isinstance(w, Event))
        self.assertEqual(w.__str__(), w.name)
        self.assertEqual(w.__unicode__(), w.name)


class AdminTest(TestCase):
    def setUp(self):
        self.asoc = Association.objects.create(id=1)
        self.admin = Administrator.objects.create(username="bob", association=self.asoc)

    def test_admin_creation(self):
        w = self.admin
        self.assertTrue(isinstance(w, Administrator))
        self.assertEqual(w.__str__(), w.username)
        self.assertEqual(w.__unicode__(), w.username)


class ProfileTest(TestCase):
    def create_profile(self):
        self.asoc = Association.objects.create()
        self.admin = Administrator.objects.create(association=self.asoc)
        return Profile.objects.get(user=self.admin)

    def test_profile_creation(self):
        w = self.create_profile()
        self.assertTrue(isinstance(w, Profile))
        self.assertEqual(w.__str__(), w.user.username)




