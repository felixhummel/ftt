from django.utils import timezone
from django.views.generic import TemplateView


class HealthView(TemplateView):
    template_name = 'ftt/health.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
