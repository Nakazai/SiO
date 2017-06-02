from django import forms
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.core.exceptions import ValidationError
from .models import Member, Association
from django_popup_view_field.fields import PopupViewField

from .popups import GenderPopupView

from SiO.settings import ALLOWED_SIGNUP_DOMAINS


# TODO: Her lages det validering


def SignupDomainValidator(value):
    if '*' not in ALLOWED_SIGNUP_DOMAINS:
        try:
            domain = value[value.index("@"):]
            if domain not in ALLOWED_SIGNUP_DOMAINS:
                raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501

        except Exception:
            raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501


def UniqueEmailValidator(value):
    if Member.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')


# def validate_gender(value):
#     if not value in ('woman', 'man', 'female', 'male'):
#         raise ValidationError(u'%s is not a valid value for gender.' % value)


CHOICES = [('Female', 'Female'),
           ('Male', 'Male')]


class RegForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'firstname', 'id': 'firstname'}),
        max_length=30,
        required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'lastname', 'id': 'lastname'}),
        max_length=30,
        required=True)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'name': 'email', 'id': 'email', 'placeholder': 'example@example.com'}),
        required=True,
        max_length=75)
    # date_of_birth = forms.DateField( initial="1990-06-21", widget=DateWidget(usel10n=True, bootstrap_version=3,
    #                                                   attrs={'name': 'date_of_birth',
    #                                                          'placeholder': 'YYYY-MM-DD or YYYY MM DD   example: 1991 03 01'},
    #                                                   ))
    date_of_birth = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3,
                                                                            attrs={'name': 'date_of_birth',
                                                                                   'placeholder': 'YYYY-MM-DD or YYYY MM DD   example: 1991 03 01'},
                                                                            ))
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'name': 'gender'}))
    # gender = PopupViewField(
    #     # ##Attrs for popup
    #     view_class=GenderPopupView,
    #     popup_dialog_title='What is your gender?',
    #     # ##Attr for CharField
    #     required=True,
    #     help_text='Enter either woman or man or female or male'
    # )
    end_date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3,
                                                 attrs={'name': 'end_date',
                                                        'placeholder': 'YYYY-MM-DD or YYYY MM DD    example: 2017-03-01'}
                                                 ))

    class Meta:
        model = Member
        exclude = ['last_login', 'date_joined']
        fields = ['first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'end_date']

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)
        self.fields['email'].validators.append(UniqueEmailValidator)
        self.fields['email'].validators.append(SignupDomainValidator)


# Defines the structure of the form that shows in template
class EditRegForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'firstname'}),
        max_length=30,
        required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'lastname'}),
        max_length=30,
        required=True)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}),
        required=True,
        max_length=75)
    date_of_birth = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3,
                                                      attrs={'name': 'date_of_birth'}))
    end_date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3,
                                                 attrs={'name': 'end_date'}))

    # Sets the permissions to be stored in the database
    class Meta:
        model = Member
        exclude = ['last_login', 'date_joined']
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'end_date']

    # The constructor is set and gets called in to views.py
    def __init__(self, *args, **kwargs):
        super(EditRegForm, self).__init__(*args, **kwargs)


class RegAsoc(forms.ModelForm):
    asoc_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)

    class Meta:
        model = Association
        fields = ['asoc_name', ]

    def __init__(self, user, *args, **kwargs):
        super(RegAsoc, self).__init__(*args, **kwargs)



