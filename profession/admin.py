from django.contrib import admin
from django.contrib.auth.models import Group

from profession.models import Profession, Sector


@admin.register(Sector)
class AdminSector(admin.ModelAdmin):
    list_display = [
        'title',
    ]


@admin.register(Profession)
class AdminProfession(admin.ModelAdmin):
    list_display = [
        'title',
    ]


admin.site.unregister(Group)
