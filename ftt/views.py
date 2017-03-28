from django.shortcuts import redirect
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
    clock_id = -1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            clock = Clock.objects.get(id=self.clock_id)
            context['start_dt'] = clock.start_dt
            context['end_dt'] = clock.end_dt
            context['comment'] = clock.comment
        except Clock.DoesNotExist:
            pass
        context['form'] = ClockForm()
        return context

    def post(self, request, *args, **kwargs):
        try:
            clock = Clock.objects.get(id=self.clock_id)
        except Clock.DoesNotExist:
            clock = Clock(id=self.clock_id)
        clock.start_dt = parse_datetime(request.POST['start_dt'])
        if request.POST['end_dt']:
            clock.end_dt = parse_datetime(request.POST['end_dt'])
        if request.POST['comment']:
            clock.comment = request.POST['comment']
        clock.save()
        return redirect('clock_start')
