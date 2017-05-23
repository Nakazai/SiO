from django.db import models


# Model of Member
class Member(models.Model):
    member_no = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True, unique=True)
    association = models.ForeignKey('Association')
    reg_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)

    # Sets the name of the table instead of "Member object"
    class Meta:
        db_table = 'Member'

    # Shows the variables as "first_name" and "last_name" instead of "object"
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class MemberSummary(Member):
    class Meta:
        proxy = True
        verbose_name = 'Member Summary'
        verbose_name_plural = 'Member Summary'


class Association(models.Model):
    asoc_name = models.CharField(max_length=50, null=True, blank=True, unique=True)

    class Meta:
        db_table = 'Association'

    def __str__(self):
        return self.asoc_name

    def __unicode__(self):
        return self.asoc_name


class AssociationSummary(Association):
    class Meta:
        proxy = True
        verbose_name = 'Association Summary'
        verbose_name_plural = 'Association Summary'




