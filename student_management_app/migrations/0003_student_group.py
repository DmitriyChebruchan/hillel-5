# Generated by Django 4.2.5 on 2023-10-07 20:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("group_management_app", "0002_alter_group_curator"),
        ("student_management_app", "0002_student_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="group",
            field=models.ManyToManyField(
                related_name="student", to="group_management_app.group"
            ),
        ),
    ]
