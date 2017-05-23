from django.contrib.auth.admin import UserAdmin, admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import Group
from SiO.CoAdmin.models import Administrator


class AdministratorCreationForm(UserCreationForm):
    union_position = forms.CharField()

    class Meta:
        model = Administrator
        fields = ("username", "union_position",)


class AdministratorChangeForm(UserChangeForm):
    union_position = forms.CharField()

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


admin.site.unregister(Group)



