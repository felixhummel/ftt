from django.http import HttpResponse
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.views.generic import ListView
from django.views.generic import TemplateView

from ftt import models
from ftt.forms import ClockForm
from ftt.models import Clock


class HealthView(TemplateView):
    template_name = 'ftt/health.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class Entries(ListView):
    model = models.Entry


class ClockView(TemplateView):
    template_name = 'ftt/clock.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ClockForm()
        return context

    def post(self, request, *args, **kwargs):
        try:
            clock = Clock.objects.get(id=-1)
        except Clock.DoesNotExist:
            clock = Clock(id=-1)
        clock.start_dt = parse_datetime(request.POST['start_dt'])
        if request.POST['end_dt']:
            clock.end_dt = parse_datetime(request.POST['end_dt'])
        if request.POST['comment']:
            clock.comment = request.POST['comment']
        clock.save()
        return HttpResponse(str(clock.end_dt - clock.start_dt), content_type='text/plain; charset=utf-8')
