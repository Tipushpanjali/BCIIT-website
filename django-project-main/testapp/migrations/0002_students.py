# Generated by Django 5.1.5 on 2025-03-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('department', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('batch', models.IntegerField()),
            ],
        ),
    ]
