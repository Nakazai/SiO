from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, UpdateView, CreateView, ListView

from datetime import datetime

# from SiO.member.models import Event, Administrator
from SiO.CoAdmin.models import Event, Administrator
from SiO.member.models import Member
from SiO.CoAdmin.models import Association

# from SiO.calapp.forms import CalForm


# def calendar(request):
#     # if request.method == 'POST':
#     #     form = CalForm(request.user, request.POST)
#     #     print(request.user.association)
#     #     asoc_pk = form.cleaned_data.get('association')
#     #     association = Association.objects.get(id=asoc_pk.pk)
#     #
#     #     Event.objects.create(
#     #         association=association
#     #     )
#     return render(request, 'calapp/calendar.html', {})


# def form_ajax(request):
#     # res = {'success': False}
#     if request.is_ajax() and request.method == 'GET':
#         # association = request.POST['association']
#         form = CalForm(request.user, request.GET)
#         # print(request.user.association)
#         asoc_pk = form.cleaned_data.get('association')
#         association = Association.objects.get(id=asoc_pk.pk)
#         # res['association'] = association
#
#         # return JsonResponse({'association': association})
#         # res['success'] = True
#         return JsonResponse(association)


class calendar(ListView):

    model = Event
    # form_class = CalForm
    template_name = 'calapp/calendar.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(calendar, self).dispatch(request, *args, **kwargs)

    # def get_queryset(self):
    #     # queryset = Event.objects.filter(name=self.request.user.association)
    #     queryset = Event.objects.filter(association=self.request.user.association)
    #     # queryset = Administrator.objects.filter(id=self.request.user.id).values('association__asoc_name')
    #     # queryset = Administrator.objects.filter(association=self.request.user.association)
    #     # association = Administrator.objects.filter(id=self.request.user.id).values('association__asoc_name')
    #     # queryset = Association.objects.get(asoc_name=association)
    #     return queryset


@login_required
def event_get(request, start, end):
    res = {'success': False}
    try:
        datetime.strptime(start, '%Y-%m-%dT%H:%M:%S.%fZ')
        datetime.strptime(end, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        res['message'] = \
            'Invalid params: ISO format start end dates expected'
        return JsonResponse(res)
    result = Event.objects.filter(
        association=request.user.association,  # Add filter
        start__range=(start, end)).order_by('start').values()

    res['data'] = list(result)
    res['success'] = True
    return JsonResponse(res)


def paramMissing(POST, param, res):
    if param not in POST:
        res['message'] = param + ' param missing'
        return True
    return False


def event_delete(request):
    if request.method == 'POST':
        res = {'success': False}

        if paramMissing(request.POST, 'eid', res):
            return JsonResponse(res)

        eid = request.POST['eid']
        Event.objects.filter(id=eid).delete()

        res['success'] = True
        res['message'] = 'deleted'
        res['eid'] = eid
        return JsonResponse(res)
    else:
        raise Http404


def event_add_edit(request):
    # if request.method == 'POST':
    #     form = CalForm(request.POST)
    #     user = request.user
    #     form.fields['association'].queryset = Association.objects.filter(asoc_name=user.association)
    if request.method == 'POST':
        # user = request.user
        # association = Association.objects.filter(asoc_name=user.association)
        # if Association == request.user:
        # form = CalForm(request.user, request.POST)
        # print(request.user.association)

        # if form.is_valid():
        # print(request.user.association)
        # form = CalForm(request.POST, user=request.user)
        res = {'success': False}
        # print(request.user.association)

        # if paramMissing(request.POST, 'name', res) \
        #         or paramMissing(request.POST, 'location', res) \
        #         or paramMissing(request.POST, 'start', res) \
        #         or paramMissing(request.POST, 'end', res) \
        #         or paramMissing(request.POST, 'allday', res) \
        #         or paramMissing(request.POST, 'description', res) \
        #         or paramMissing(request.POST, 'action', res) \
        #         or paramMissing(request.POST, 'synced', res):
        #     return JsonResponse(res)

        # print(request.user.association)
        # association = form.request.POST('association')
            # asoc_pk = request.POST.get('association')
            # association = Association.objects.get(id=asoc_pk.pk)
        # res = {
        #     'association': association,
        #     'success': False
        # }
        # print(association)
        gid = request.POST.get('gid', '')
        # asoc_pk = form.cleaned_data.get('association')
        # asoc = Association.objects.get(id=asoc_pk.pk)
        # or paramMissing(request.POST, 'association', res) \ som ska være ovenfor

        # asoc_pk = form.request.POST['association']
        # asoc_pk = form.request('association')
        # association = Association.objects.get(id=asoc_pk.pk)
        # association = form.cleaned_data.get('association')
        # print(association)
        action = request.POST['action']
        name = request.POST['name']
        location = request.POST['location']
        start = request.POST['start']
        end = request.POST['end']
        allday = request.POST['allday'] == 'true'
        description = request.POST['description']
        synced = request.POST['synced'] == 'true'
        # association = Association.objects.filter(asoc_name=request.user.association).values('administrator__association')
        # association = Association.objects.filter(administrator=request.user.id).values('asoc_name')
        # association = Association.objects.filter(administrator=request.user.id).filter(asoc_name=request.user.association)
        # association = Association.objects.filter(asoc_name=request.user.association)
        # association = Event.objects.filter(association__user__id=request.user.id)
        association = Administrator.objects.filter(id=request.user.id).values('association__asoc_name')
        asoc = Association.objects.get(asoc_name=association)
        # association = Association.objects.filter(asoc_name=request.user.association)
        # asoc = Event.objects.get(association=association)
        # asoc = Association.objects.filter(asoc_name=request.user.association)
        # association = Event.objects.get(association_id=asoc)
        # if association == asoc:
        # user = Administrator.objects.filter(username=request.user)
        # asoc = Administrator.objects.get(id=user)
        # association = form.request.POST['association']
        # asoc_pk = form.request.POST['association']
        # association = Association.objects.get(id=asoc_pk.pk)
        # print(association)
        # asoc_id = request.POST.get('association')
        # association = Association.objects.get(pk=asoc_id)

        # if paramMissing(request.POST, 'name', res) \
        #         or paramMissing(request.POST, 'location', res) \
        #         or paramMissing(request.POST, 'start', res) \
        #         or paramMissing(request.POST, 'end', res) \
        #         or paramMissing(request.POST, 'allday', res) \
        #         or paramMissing(request.POST, 'description', res) \
        #         or paramMissing(request.POST, 'action', res) \
        #         or paramMissing(request.POST, 'synced', res):
        #     return JsonResponse(res)

        if action == 'add':
            Event.objects.create(
                name=name,
                location=location,
                start=start,
                end=end,
                allday=allday,
                description=description,
                synced=synced,
                gid=gid,
                association=asoc
            )

            # res['association'] = association
            res['success'] = True
            res['message'] = 'added'
            eid = Event.objects.latest('id').id
            res['eid'] = eid
            res['data'] = Event.objects.values().get(id=eid)

            # return JsonResponse(res,  {'form': CalForm(request.user)})
        elif action == 'edit':

            if paramMissing(request.POST, 'eid', res):
                return JsonResponse(res)

            eid = request.POST['eid']
            event = Event.objects.get(id=eid)
            event.name = name
            event.location = location
            event.start = start
            event.end = end
            event.allday = allday
            event.description = description
            event.synced = synced
            event.save()

            res['success'] = True
            res['message'] = 'edited'
            res['eid'] = eid
            res['data'] = Event.objects.values().get(id=eid)

        # return JsonResponse(res,  {'form': CalForm(request.user)})
        return JsonResponse(res)
    else:
        raise Http404


def event_setsync(request):
    if request.method == 'POST':
        res = {'success': False}

        if paramMissing(request.POST, 'eid', res) \
                or paramMissing(request.POST, 'gid', res):
            return JsonResponse(res)

        eid = request.POST['eid']
        gid = request.POST['gid']

        event = Event.objects.get(id=eid)
        event.synced = True
        event.gid = gid
        event.save()

        res['success'] = True
        res['message'] = 'sync set'
        res['eid'] = eid
        res['gid'] = gid
        return JsonResponse(res)
    else:
        raise Http404




















# from calendar import monthrange
# from sched import Event
# #
# from django.shortcuts import render, render_to_response
# # from django.template import RequestContext
# from django.utils.datetime_safe import datetime, date
#
#
# def named_month(month_number):
#     """
#     Return the name of the month, given the number.
#     """
#     return date(1900, month_number, 1).strftime("%B")
#
#
# def this_month(request):
#     """
#     Show calendar of calapp this month.
#     """
#     today = datetime.now()
#     return events(request, today.year, today.month)
#
#
# def events(request, year, month, series_id=None):
#     """
#     Show calendar of calapp for a given month of a given year.
#     ``series_id``
#     The event series to show. None shows all event series.
#
#     """
#
#     my_year = int(year)
#     my_month = int(month)
#     my_calendar_from_month = datetime(my_year, my_month, 1)
#     my_calendar_to_month = datetime(my_year, my_month, monthrange(my_year, my_month)[1])
#
#     my_events = Event.objects.filter(date_and_time__gte=my_calendar_from_month).filter(date_and_time__lte=my_calendar_to_month)
#     if series_id:
#         my_events = my_events.filter(series=series_id)
#
#     # Calculate values for the calendar controls. 1-indexed (Jan = 1)
#     my_previous_year = my_year
#     my_previous_month = my_month - 1
#     if my_previous_month == 0:
#         my_previous_year = my_year - 1
#         my_previous_month = 12
#     my_next_year = my_year
#     my_next_month = my_month + 1
#     if my_next_month == 13:
#         my_next_year = my_year + 1
#         my_next_month = 1
#     my_year_after_this = my_year + 1
#     my_year_before_this = my_year - 1
#     return render(request, 'calapp/events.html', {'events_list': my_events,
#                                                   'month': my_month,
#                                                   'month_name': named_month(my_month),
#                                                   'year': my_year,
#                                                   'previous_month': my_previous_month,
#                                                   'previous_month_name': named_month(my_previous_month),
#                                                   'previous_year': my_previous_year,
#                                                   'next_month': my_next_month,
#                                                   'next_month_name': named_month(my_next_month),
#                                                   'next_year': my_next_year,
#                                                   'year_before_this': my_year_before_this,
#                                                   'year_after_this': my_year_after_this})
# # , context_instance=RequestContext(request))
