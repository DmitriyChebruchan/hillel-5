from django.db import models

from group_management_app.models import Group

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=130)
    surname = models.CharField(max_length=130)
    year = models.PositiveIntegerField(null=True)
    group = models.ManyToManyField(Group, related_name="student")
    phone_number = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.first_name}"
