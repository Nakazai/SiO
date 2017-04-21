from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import Count, Sum, Min, Max
from django.db.models.functions import Trunc

from SiO.member.models import Association, AssociationSummary, Member


@admin.register(AssociationSummary)
class ChartAssociationAdmin(admin.ModelAdmin):
    change_list_template = 'admin/chart_association.html'
    # change_list_template = 'admin/SiO/extras/sometemplate_change_form.html'
    # date_hierarchy = 'reg_date'

    # def get_total(self):
    #     # total = Member.objects.all().aggregate(association=Sum('member_no'))
    #     total = Member.objects.all().count()
    #     return total
    #
    # def changelist_view(self, request, extra_context=None):
    #     my_context = {
    #         'total members': self.get_total(),
    #     }
    #     return super(ChartAssociationAdmin, self).changelist_view(request,
    #                                                               extra_context=my_context)

    def changelist_view(self, request, extra_context=None):
        response = super(ChartAssociationAdmin, self).changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
            # qs = Association.objects.all()
            # qs1 = Association.objects.filter(association=self.association).count()
            # qs = Member.objects.filter(association=self.association).count()
        except (AttributeError, KeyError):
            return response

        metrics = {
        'association': Count('asoc_name'),
        'total': Sum('member'),
        # 'total_sales': Sum('price'),
        }
        response.context_data['summary'] = list(
            qs.values('asoc_name', 'member').annotate(**metrics)
            # qs2.values('member__asoc_name'),
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )

        # summary_over_time = qs.annotate(
        #     period=Trunc(
        #         'member',
        #         'asoc_name',
        #         # output_field=DateTimeField(),
        #     ),
        # ).values('period').annotate(total=Sum('member'))
            # .order_by('period')
        # summary_over_time = qs.values('asoc_name', 'member').annotate(total=Sum('member'))
        summary_over_time = qs.values('asoc_name',).annotate(total=Sum('member'))

        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)

        response.context_data['summary_over_time'] = [{
                                                          'asoc_name': x['asoc_name'],
                                                          'total': x['total'] or 0,
                                                          'pct':\
                                                              ((x['total'] or 0) - low) / (high - low) * 100
                                                              if high > low else 0,
                                                      } for x in summary_over_time]

        return response


# admin.site.register(Association, ChartAssociationAdmin)
