from django.shortcuts import render, get_object_or_404
from testapp.models import Faculty
from testapp.models import Event, students, OldEvent
from datetime import date


def sync_events():
    today = date.today()

    past_events = Event.objects.filter(date__lt=today)
    for event in past_events:
        OldEvent.objects.create(
            title=event.title,
            date=event.date,
            location=event.location,
            description=event.description,
            image=event.image
        )
        event.delete()

    future_events = OldEvent.objects.filter(date__gte=today)
    for old_event in future_events:
        Event.objects.create(
            title=old_event.title,
            date=old_event.date,
            location=old_event.location,
            description=old_event.description,
            image=old_event.image
        )
        old_event.delete()


def home(request):
    sync_events()
  
    events = list(OldEvent.objects.all().order_by('date'))
    return render(request, 'testapp/home.html', {'events': events})

def about(request):
    return render(request, 'testapp/aboutus.html')

def student(request):
    students1 = list(students.objects.all())
    return render(request, 'testapp/student.html', {'students': students1})


def faculty_list(request):
    faculties = list(Faculty.objects.all())
    return render(request, 'testapp/faculty.html', {'faculties': faculties})

def events_list(request):
    sync_events()
    events = list(Event.objects.all().order_by('date'))

    return render(request, 'testapp/events.html', {'events': events})

def faculty_detail(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    return render(request, 'testapp/facultyDetails.html', {'faculty': faculty})
