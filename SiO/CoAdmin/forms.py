from django import forms
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# from django.contrib.auth.models import AbstractUser as Admin
from .models import Administrator
from SiO.settings import ALLOWED_SIGNUP_DOMAINS
from SiO.member.models import Association

# TODO: Her lages det validering
def SignupDomainValidator(value):
    if '*' not in ALLOWED_SIGNUP_DOMAINS:
        try:
            domain = value[value.index("@"):]
            if domain not in ALLOWED_SIGNUP_DOMAINS:
                raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501

        except Exception:
            raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501


def ForbiddenUsernamesValidator(value):
    forbidden_usernames = ['member', 'settings', 'news', 'about', 'help',
                           'signin', 'signup', 'signout', 'terms', 'privacy',
                           'cookie', 'new', 'login', 'logout', 'administrator',
                           'join', 'account', 'username', 'root', 'blog',
                           'user', 'users', 'billing', 'subscribe', 'reviews',
                           'review', 'blog', 'blogs', 'edit', 'mail', 'email',
                           'home', 'job', 'jobs', 'contribute', 'newsletter',
                           'shop', 'profile', 'register', 'auth',
                           'member', 'campaign', 'config', 'delete',
                           'remove', 'forum', 'forums', 'download',
                           'downloads', 'contact', 'blogs', 'feed', 'feeds',
                           'faq', 'intranet', 'log', 'registration', 'search',
                           'explore', 'rss', 'support', 'status', 'static',
                           'media', 'setting', 'css', 'js', 'follow',
                           'activity', 'questions', 'articles', 'network', ]

    if value.lower() in forbidden_usernames:
        raise ValidationError('This is a reserved word.')


def InvalidUsernameValidator(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('Enter a valid username.')


def UniqueEmailValidator(value):
    if Administrator.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')


def UniqueUsernameIgnoreCaseValidator(value):
    if Administrator.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this Username already exists.')


# def CanNotChangeAssociation(value):
#     if not Administrator.objects.filter(association=value):
#         raise ValidationError('Admin can not change association.')


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    association = forms.ModelChoiceField(queryset=Association.objects.all(),
                                         widget=forms.Select(attrs={'class': 'form-control'}),
                                         required=True)

    # association_choices = [(i['pk'], i['asoc_name'])
    #                        for i in Association.objects.values('pk', 'asoc_name')]
    # association = forms.ChoiceField(choices=association_choices, widget=forms.Select(attrs={'class': 'form-control'}),
    #                                 required=True)

    # association_choices = [(i['asoc_name'], i['asoc_name'])
    #                        for i in Association.objects.values('asoc_name')]
    # asoc_name = forms.ChoiceField(choices=association_choices,widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    # association = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'}),
    #     max_length=30,
    #     required=True)
    union_position = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True,
        help_text='Usernames may contain <strong>alphanumeric</strong>, <strong>_</strong> and <strong>.</strong> characters')  # noqa: E261
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm your password",
        required=True)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
        max_length=75)

    # def save(self, commit=True):
    #     instance = super(SignUpForm, self).save(commit=False)
    #     asoc = self.cleaned_data['association']
    #     instance.association = Association.objects.get(pk=asoc)
    #     instance.save(commit)
    #     return instance

    class Meta:
        model = Administrator
        exclude = ['last_login', 'date_joined',]
        fields = ['first_name', 'last_name', 'association', 'union_position', 'username', 'email', 'password', 'confirm_password', ]

    # user = None
    # usergroups = None
    # association = forms.ModelChoiceField(queryset=usergroups,
    #                                      widget=forms.Select(attrs={'class': 'form-control'}),
    #                                      required=True)

    def __init__(self, *args, **kwargs):
        # self.user = user
        # self.request = request
        super(SignUpForm, self).__init__(*args, **kwargs)
        # self.fields['association'].queryset = Administrator.objects.filter(association=self.request.user.association)
        # super(SignUpForm, self).__init__(*args, **kwargs)
        # self.fields['association'].queryset = qs
        # instance = getattr(self, 'instance', None)
        # if instance and instance.pk:
        #     self.fields['association'].widget.attrs['disabled'] = True
        # self.fields['username'].validators.append(ForbiddenUsernamesValidator)
        # self.fields['username'].validators.append(InvalidUsernameValidator)
        # self.fields['username'].validators.append(
        #     UniqueUsernameIgnoreCaseValidator)
        # self.fields['email'].validators.append(UniqueEmailValidator)
        self.fields['email'].validators.append(SignupDomainValidator)

    # def clean_assoc(self):
    #     assoc = self.request.user

    # def clean_sku(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         return instance.sku
    #     else:
    #         return self.cleaned_data['association']

    # def get_queryset(self):
    #     qs = Administrator.objects.filter(association=self.request.user.association)
    #     super(SignUpForm, self).get_queryset()
    #     self.fields['association'].queryset = qs

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(
                ['Passwords don\'t match'])
        return self.cleaned_data


class EditSignUpForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    # association = forms.ModelChoiceField(queryset=Association.objects.all(),
    #                                      widget=forms.Select(attrs={'class': 'form-control'}),
    #                                      required=True)
    union_position = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True,
        help_text='Usernames may contain <strong>alphanumeric</strong>, <strong>_</strong> and <strong>.</strong> characters')  # noqa: E261
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
        max_length=75)

    class Meta:
        model = Administrator
        exclude = ['last_login', 'date_joined']
        fields = ['first_name', 'last_name', 'union_position', 'username', 'email', ]

    def __init__(self, *args, **kwargs):
        super(EditSignUpForm, self).__init__(*args, **kwargs)
        # self.fields['username'].validators.append(ForbiddenUsernamesValidator)
        # self.fields['username'].validators.append(InvalidUsernameValidator)
        # self.fields['username'].validators.append(
        #     UniqueUsernameIgnoreCaseValidator)
        # self.fields['email'].validators.append(UniqueEmailValidator)
        self.fields['email'].validators.append(SignupDomainValidator)
        # self.fields['association'].validators.append(CanNotChangeAssociation)


class InnsideSignUpForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    # association = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    association = forms.ModelChoiceField(queryset=Association.objects.none(),
                                         widget=forms.Select(attrs={'class': 'form-control'}),
                                         required=True)
    union_position = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True,
        help_text='Usernames may contain <strong>alphanumeric</strong>, <strong>_</strong> and <strong>.</strong> characters')  # noqa: E261
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
        max_length=75)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm your password",
        required=True)

    class Meta:
        model = Administrator
        exclude = ['last_login', 'date_joined']
        fields = ['first_name', 'last_name', 'association', 'union_position', 'username', 'email', 'password', 'confirm_password', ]

    def __init__(self, user, *args, **kwargs):
        super(InnsideSignUpForm, self).__init__(*args, **kwargs)
        self.fields['association'].queryset = Association.objects.filter(asoc_name=user.association)

        # self.fields['username'].validators.append(ForbiddenUsernamesValidator)
        # self.fields['username'].validators.append(InvalidUsernameValidator)
        # self.fields['username'].validators.append(
        #     UniqueUsernameIgnoreCaseValidator)
        # self.fields['email'].validators.append(UniqueEmailValidator)
        self.fields['email'].validators.append(SignupDomainValidator)
        # self.fields['association'].validators.append(CanNotChangeAssociation)
        # self.fields['association'].widget.attrs['readonly'] = True


class ChangePasswordForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Old password",
        required=True)

    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New password",
        required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm new password",
        required=True)

    class Meta:
        model = Administrator
        fields = ['id', 'old_password', 'new_password', 'confirm_password']

    def clean(self):
        super(ChangePasswordForm, self).clean()
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        id = self.cleaned_data.get('id')
        user = Administrator.objects.get(pk=id)
        if not user.check_password(old_password):
            self._errors['old_password'] = self.error_class([
                'Old password don\'t match'])
        if new_password and new_password != confirm_password:
            self._errors['new_password'] = self.error_class([
                'Passwords don\'t match'])
        return self.cleaned_data



