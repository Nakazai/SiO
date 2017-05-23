from django.test import TestCase
from SiO.member.models import Association, Member
from django.utils import timezone
from django.core.urlresolvers import reverse

# models test


class AssociationTest(TestCase):

    def create_association(self, asoc_name="dortmund"):
        return Association.objects.create(asoc_name=asoc_name)

    def test_association_creation(self):
        w = self.create_association()
        self.assertTrue(isinstance(w, Association))
        self.assertEqual(w.__str__(), w.asoc_name)
        self.assertEqual(w.__unicode__(), w.asoc_name)


class MemberTest(TestCase):

    def create_member(self, first_name="foo", last_name="test"):
        self.asoc = Association.objects.create(id=1)
        return Member.objects.create(first_name=first_name, last_name=last_name, association=self.asoc)

    def test_member_creation(self):
        w = self.create_member()
        self.assertTrue(isinstance(w, Member))
        self.assertEqual(w.__str__(), w.first_name + ' ' + w.last_name)


