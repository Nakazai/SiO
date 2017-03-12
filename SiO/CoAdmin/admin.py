from django.contrib.auth.admin import UserAdmin, admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.contrib import CoAdmin

from SiO.CoAdmin.models import Administrator, Association

# TODO: UserAdmin gir en fin grensesnitt med change password osv


class AdministratorCreationForm(UserCreationForm):
    union_position = forms.CharField()
    # association = forms.ModelChoiceField(queryset=Association.objects.all(),
    #                                      widget=forms.Select(attrs={'class': 'form-control'}),
    #                                      required=True)

    class Meta:
        model = Administrator
        fields = ("username", "union_position",)


class AdministratorChangeForm(UserChangeForm):
    union_position = forms.CharField()
    # association = forms.ModelChoiceField(queryset=Association.objects.all(),
    #                                      widget=forms.Select(attrs={'class': 'form-control'}),
    #                                      required=True)

    class Meta:
        model = Administrator
        fields = ("username", "union_position",)


class AdministratorAdmin(UserAdmin):
    form = AdministratorChangeForm
    add_form = AdministratorCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('union_position', 'association', 'first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'union_position', 'association', )}
         ),
    )


admin.site.register(Administrator, AdministratorAdmin)


admin.site.register(Association)

admin.site.unregister(Group)




# TODO: Ovenfor skal være med mens nedenfor må være kommentert





# class AssociationAdmin(UserAdmin):
#     pass


# from django.contrib import CoAdmin
# from SiO.CoAdmin.models import Administrator
#
# CoAdmin.site.register(Administrator)


# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = Administrator
#         fields = ['first_name', 'last_name', 'association', 'union_position', 'username', 'email', ]
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with CoAdmin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()
#
#     class Meta:
#         model = Administrator
#         fields = ['first_name', 'last_name', 'association', 'union_position', 'username', 'email', ]
#
#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]
#
#
# class AdministratorAdmin(UserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'date_of_birth', 'is_admin')
#     list_filter = ('is_admin',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('date_of_birth',)}),
#         ('Permissions', {'fields': ('is_admin',)}),
#         ('Important dates', {'fields': ('last_login',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'date_of_birth', 'password1', 'password2')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()
#
# # Now register the new UserAdmin...
# CoAdmin.site.register(Administrator, AdministratorAdmin)

