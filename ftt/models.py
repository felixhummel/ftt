from django.db import models
from django.utils.functional import cached_property
from mptt.models import MPTTModel, TreeForeignKey


class Project(MPTTModel):
    name = models.CharField(max_length=128)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    @cached_property
    def full_name(self):
        parts = self.get_ancestors(ascending=False, include_self=True).all()
        return '/'.join([p.name for p in parts])

    def __str__(self):
        return self.full_name


class Entry(models.Model):
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()
    project = models.ForeignKey('Project')
    comment = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-start_dt']

    def __str__(self):
        start_day = self.start_dt.strftime('%m-%d')
        start_time = self.start_dt.strftime('%H:%M')
        end_time = self.end_dt.strftime('%H:%M')
        return f'{start_day} {start_time}-{end_time} {self.comment}'


class Clock(models.Model):
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField(null=True)
    comment = models.TextField(null=True, blank=True)

    @property
    def delta(self):
        if not self.end_dt:
            return None
        return self.end_dt - self.start_dt
