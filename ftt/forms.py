from django.forms import ModelForm, widgets

from ftt.models import Clock


class ClockForm(ModelForm):
    class Meta:
        model = Clock
        fields = ['start_dt', 'end_dt', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_dt'].widget = widgets.SplitDateTimeWidget()
        self.fields['end_dt'].widget = widgets.SplitDateTimeWidget()
