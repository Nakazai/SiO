from django.contrib import admin
from SiO.CoAdmin.models import Event


# class EventAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return False
#
#     def has_edit_permission(self, request, obj=None):
#         return False

    # def has_change_permission(self, request, obj=None):
    #     if obj is not None and obj > 1:
    #         return False
    #     return super(EventAdmin, self).has_change_permission(request, obj=obj)


# class ReadOnlyMixin(admin.ModelAdmin): # Add inheritance from "object" if using Python 2
#     list_display_links = None

# admin.site.register(Event, EventAdmin)
admin.site.register(Event)

