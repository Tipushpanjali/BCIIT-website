from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    Qualification = models.CharField(max_length=100)
    subjects = models.TextField()
    photo = models.ImageField(upload_to='faculty_photos/', null=True, blank=True)
    

    def _str_(self):
        return self.name
   

class students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    batch = models.IntegerField()
    photo=models.ImageField(upload_to='student_photos/', null=True, blank=True)

    def _str_(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField() 
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def _str_(self):
        return self.title
    
class OldEvent(models.Model):  
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='old_event_images/', blank=True, null=True)

    def __str__(self):  
        return self.title
