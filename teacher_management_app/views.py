from django.shortcuts import redirect, render

from teacher_management_app.models import Teacher

from .forms import TeacherForm


def show_teachers(request):
    all_teachers = Teacher.objects.all()
    return render(request, "teacher/list_of_teachers.html",
                  {"data": all_teachers})


def create_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/teachers/")

    else:
        if request.method == "GET":
            form = TeacherForm()

    return render(request, "teacher/teacher_form.html", {"form": form})
