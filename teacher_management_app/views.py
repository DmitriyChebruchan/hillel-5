from django.shortcuts import render
from teacher_management_app.models import Teacher


def show_teachers(request):
    all_teachers = Teacher.objects.all()
    return render(request, "list_of_teachers.html", {"data": all_teachers})
