from django.contrib.auth.admin import UserAdmin, admin
from SiO.member.models import Member, Association
# from SiO.CoAdmin.models import Member, Association


# class MemberAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'association')
#     search_fields = ['first_name', 'last_name', ]
#     # list_filter = ('first_name', 'last_name',)
#
#
# admin.site.register(Member, MemberAdmin)


class AssociationAdmin(admin.ModelAdmin):
    list_display = ('asoc_name',)
    search_fields = ['asoc_name', ]
    # list_filter = ('asoc_name',)


admin.site.register(Association, AssociationAdmin)
