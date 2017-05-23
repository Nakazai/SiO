from django.contrib import admin
from django.db.models import Count

from SiO.member.models import  AssociationSummary


@admin.register(AssociationSummary)
class ChartAssociationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    change_list_template = 'admin/chart_association.html'

    def changelist_view(self, request, extra_context=None):
        response = super(ChartAssociationAdmin, self).changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
        'total': Count('member'),
        }
        response.context_data['summary'] = list(
            qs.values('asoc_name').annotate(**metrics)
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )

        return response





