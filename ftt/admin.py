from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Project, Entry


@admin.register(Project)
class ProjectAdmin(MPTTModelAdmin):
    pass


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
