# Generated by Django 5.1.5 on 2025-03-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_faculty_description_faculty_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='student_photos/'),
        ),
    ]
