# Generated by Django 4.2 on 2023-05-02 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("studentManagementApp", "0004_rename_staff_subjects_teacher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subjects",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="studentManagementApp.teachers",
            ),
        ),
        migrations.AlterField(
            model_name="teachers",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teacheruser",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("HOD", "HOD"),
                    ("Student", "Student"),
                    ("Teacher", "Teacher"),
                ],
                max_length=20,
            ),
        ),
    ]
