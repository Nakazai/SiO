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

    def create_member(self, first_name="miriam"):
        return Member.objects.create(first_name=first_name, association=1)

# views (uses reverse)

    # def test_association_list_view(self):
    #     w = self.create_member()
    #     url = reverse("views.member_overview.as_view()")
    #     resp = self.client.get(url)
    #
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertIn(w.first_name, resp.content)
