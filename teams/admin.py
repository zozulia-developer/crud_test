from django.contrib import admin

from .models import Person, Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'team')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('team',)
    list_select_related = ('team',)
