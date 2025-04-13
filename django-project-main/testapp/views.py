from django.shortcuts import render, get_object_or_404
from testapp.models import Faculty
from testapp.models import Event, students
from datetime import date

def home(request):
    return render(request, 'testapp/home.html')

def student(request):
    students1 = list(students.objects.all())
    return render(request, 'testapp/student.html', {'students': students1})


def faculty_list(request):
    faculties = list(Faculty.objects.all())
    return render(request, 'testapp/faculty.html', {'faculties': faculties})

def events_list(request):
    events = list(Event.objects.all().order_by('date'))

    return render(request, 'testapp/events.html', {'events': events})

def faculty_detail(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    return render(request, 'testapp/facultyDetails.html', {'faculty': faculty})
