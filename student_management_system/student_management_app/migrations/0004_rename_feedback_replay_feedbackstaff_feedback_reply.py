# Generated by Django 5.0 on 2024-01-05 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0003_alter_leavereportstaff_leave_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbackstaff',
            old_name='feedback_replay',
            new_name='feedback_reply',
        ),
    ]
