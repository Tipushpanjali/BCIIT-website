from django.contrib import admin
from testapp.models import Faculty, Event, students, OldEvent

admin.site.register(Faculty)
admin.site.register(Event)
admin.site.register(students)
admin.site.register(OldEvent)