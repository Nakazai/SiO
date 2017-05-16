from django.test import Client
from django.test import TestCase
from SiO.CoAdmin.models import Event, Association, Administrator, Profile
from django.utils import timezone
from django.core.urlresolvers import reverse

# models test


class EventTest(TestCase):

    # def create_Event(self, name="LAN"):
    #     return Event.objects.create(name=name, start=timezone.now(), end=timezone.now(), allday=False, synced=True,
    #                                 association=1)
    #
    # def test_event_creation(self):
    #     w = self.create_Event()
    #     self.assertTrue(isinstance(w, Event))
    #     self.assertEqual(w.__unicode__(), w.name)

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

    # def setUp(self):
    #     self.asoc = Association.objects.create(id=1)
    #     self.event = Event.objects.create(name="LAN",
    #                                       start=timezone.now(),
    #                                       end=timezone.now(),
    #                                       allday=False,
    #                                       synced=True,
    #                                       association=self.asoc)
    #     self.c = Client()
    #
    # def test_event_creation(self):
    #     w = self.event
    #     self.assertTrue(isinstance(w, Event))
    #     self.assertEqual(w.__str__(), w.name)
    #     self.assertEqual(w.__unicode__(), w.name)


class ProfileTest(TestCase):
    # def setUp(self):
        # ##self.asoc = Association.objects.create(id=2)
        # self.user = Administrator.objects.create(id=2)
        # self.username = Profile.objects.create(username="biri", user=self.user)
        # ##self.prof = Profile.objects.get_or_create(user_id=self.admin)

        # ##self.c = Client()

    # def create_profile(self):
    #     self.asoc = Association.objects.create(id=2)
    #     self.admin = Administrator.objects.create(association=self.asoc)
    #     self.user = Profile.objects.create(administrator=3)
    #     return Profile.objects.get_or_create(user=self.user, administrator=self.admin)

    # def create_profile(self):
    #     self.asoc = Association.objects.create(id=7)
    #     self.admin = Administrator.objects.create(id=6, association=self.asoc)
    #     self.user = Profile.objects.create(id=self.admin.id)
    #     return Profile.objects.get(user=self.user, administrator=self.admin)

    def create_profile(self):
        self.asoc = Association.objects.create()
        self.admin = Administrator.objects.create(association=self.asoc)
        # print(self.admin)
        # self.user = Profile.objects.create(user=self.admin)
        # print(user.query)
        return Profile.objects.get(user=self.admin)

    def test_profile_creation(self):
        w = self.create_profile()
        self.assertTrue(isinstance(w, Profile))
        self.assertEqual(w.__str__(), w.user.username)




