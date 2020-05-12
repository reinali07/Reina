from django.contrib import admin
from .models import Session, Experiment

# Register your models here.

class ExperimentInline(admin.TabularInline):
    model = Experiment
    extra = 1


class SessionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['filename']}),
    ]
    inlines = [ExperimentInline]

admin.site.register(Session, SessionAdmin)
admin.site.register(Experiment)