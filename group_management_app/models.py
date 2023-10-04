from django.db import models

from teacher_management_app.models import Teacher


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=50)
    curator = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}"
