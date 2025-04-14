

from django.contrib import admin
from .models import Faculty, students, Event, OldEvent

# Register your models here.

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'Qualification', 'subjects')
    search_fields = ('name', 'email', 'Qualification')
    list_filter = ('Qualification',)

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'course', 'batch')
    search_fields = ('name', 'email', 'department', 'course')
    list_filter = ('department', 'course', 'batch')

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    search_fields = ('title', 'location')
    list_filter = ('date', 'location')

class OldEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    search_fields = ('title', 'location')
    list_filter = ('date', 'location')

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(students, StudentsAdmin)
admin.site.register(OldEvent, OldEventAdmin)
