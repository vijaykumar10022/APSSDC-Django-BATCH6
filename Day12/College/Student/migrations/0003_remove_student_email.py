# Generated by Django 3.0.7 on 2020-09-25 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_student_phno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
    ]
