# Generated by Django 5.0 on 2024-01-05 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0004_rename_feedback_replay_feedbackstaff_feedback_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(),
        ),
    ]
