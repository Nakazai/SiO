from datetime import date
from django.utils.html import conditional_escape as esc
from django.utils.safestring import mark_safe
from itertools import groupby
from calendar import HTMLCalendar, monthrange


class ContestCalendar(HTMLCalendar):

    def __init__(self, pContestEvents):
        super(ContestCalendar, self).__init__()
        self.contest_events = self.group_by_day(pContestEvents)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.contest_events:
                cssclass += ' filled'
                body = []
                for contest in self.contest_events[day]:
                    body.append('<a href="%s">' % contest.get_absolute_url())
                    body.append(esc(contest.contest.name))
                    body.append('</a><br/>')
                return self.day_cell(cssclass, '<div class="dayNumber">%d</div> %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, '<div class="dayNumber">%d</div>' % day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month, **kwargs):
        self.year, self.month = year, month
        return super(ContestCalendar, self).formatmonth(year, month)

    def group_by_day(self, pContestEvents):
        field = lambda contest: contest.date_of_event.day
        return dict(
            [(day, list(items)) for day, items in groupby(pContestEvents, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)
































# from calendar import HTMLCalendar, month
# from django import template
# from datetime import date
# from itertools import groupby
#
# from django.utils.html import conditional_escape as esc
#
# register = template.Library()
#
#
# def do_event_calendar(parser, token):
#     """
#     The template tag's syntax is {% event_calendar year month event_list %}
#     """
#
#     try:
#         tag_name, year, month, event_list = token.split_contents()
#     except ValueError:
#         return
#     return EventCalendarNode(year, month, event_list)
#
#
# class EventCalendarNode(template.Node):
#     """
#     Process a particular node in the template. Fail silently.
#     """
#
#     def __init__(self, year, month, event_list):
#         try:
#             self.year = template.Variable(year)
#             self.month = template.Variable(month)
#             self.event_list = template.Variable(event_list)
#         except ValueError:
#             raise template.TemplateSyntaxError
#
#     def render(self, context):
#         try:
#             # Get the variables from the context so the method is thread-safe.
#             my_event_list = self.event_list.resolve(context)
#             my_year = self.year.resolve(context)
#             my_month = self.month.resolve(context)
#             cal = EventCalendar(my_event_list)
#             return cal.formatmonth(int(my_year), int(my_month))
#         except ValueError:
#             return
#         except template.VariableDoesNotExist:
#             return
#
#
# class EventCalendar(HTMLCalendar):
#     """
#     Overload Python's calendar.HTMLCalendar to add the appropriate events to
#     each day's table cell.
#     """
#
#     def __init__(self, events):
#         super(EventCalendar, self).__init__()
#         self.year, self.month = self.year, month
#         self.events = self.group_by_day(events)
#
#     def formatday(self, day, weekday):
#         if day != 0:
#             cssclass = self.cssclasses[weekday]
#             if date.today() == date(self.year, self.month, day):
#                 cssclass += ' today'
#             if day in self.events:
#                 cssclass += ' filled'
#                 body = ['<ul>']
#                 for event in self.events[day]:
#                     body.append('<li>')
#                     body.append('<a href="%s">' % event.get_absolute_url())
#                     body.append(esc(event.series.primary_name))
#                     body.append('</a></li>')
#                 body.append('</ul>')
#                 return self.day_cell(cssclass, '<span class="dayNumber">%d</span> %s' % (day, ''.join(body)))
#             return self.day_cell(cssclass, '<span class="dayNumberNoEvents">%d</span>' % day)
#         return self.day_cell('noday', '&nbsp;')
#
#     def formatmonth(self, year, month, **kwargs):
#         return super(EventCalendar, self).formatmonth(year, month)
#
#     def group_by_day(self, events):
#         field = lambda event: event.date_and_time.day
#         return dict(
#             [(day, list(items)) for day, items in groupby(events, field)]
#         )
#
#     def day_cell(self, cssclass, body):
#         return '<td class="%s">%s</td>' % (cssclass, body)
#
#     register.tag("event_calendar", do_event_calendar)
