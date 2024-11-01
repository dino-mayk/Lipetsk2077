from django.contrib import admin

from event.models import Event


@admin.register(Event)
class AdminEvents(admin.ModelAdmin):
    list_display = [
        'title',
    ]
