from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from datetime import datetime

from SiO.CoAdmin.models import Event, Administrator
from SiO.CoAdmin.models import Association


class calendar(ListView):

    model = Event
    template_name = 'calapp/calendar.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(calendar, self).dispatch(request, *args, **kwargs)


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
        association=request.user.association,
        start__range=(start, end)).order_by('start').values()

    res['data'] = list(result)
    res['success'] = True
    return JsonResponse(res)


def paramMissing(POST, param, res):
    if param not in POST:
        res['message'] = param + ' param missing'
        return True
    return False


@login_required
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


@login_required
def event_add_edit(request):
    if request.method == 'POST':
        res = {'success': False}

        gid = request.POST.get('gid', '')
        action = request.POST['action']
        name = request.POST['name']
        location = request.POST['location']
        start = request.POST['start']
        end = request.POST['end']
        allday = request.POST['allday'] == 'true'
        description = request.POST['description']
        synced = request.POST['synced'] == 'true'
        association = Administrator.objects.filter(id=request.user.id).values('association__asoc_name')
        asoc = Association.objects.get(asoc_name=association)

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

            res['success'] = True
            res['message'] = 'added'
            eid = Event.objects.latest('id').id
            res['eid'] = eid
            res['data'] = Event.objects.values().get(id=eid)

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

        return JsonResponse(res)
    else:
        raise Http404


@login_required
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





