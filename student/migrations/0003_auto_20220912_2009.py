# Generated by Django 3.0.5 on 2022-09-12 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='profile_pic',
        ),
    ]
