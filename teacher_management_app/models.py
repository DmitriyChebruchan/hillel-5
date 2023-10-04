from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=150)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.patronymic} {self.surname}"
