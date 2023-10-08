from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

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


def edit_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)

    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(request, "teacher/edit_teacher.html", {"form": form})

    form = TeacherForm(request.POST, instance=teacher)

    if "delete" in request.POST:
        try:
            teacher.delete()
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"},
                                status=500)

    if form.is_valid():
        form.save()
        return redirect(reverse("list_of_teachers"))

    return render(request, "teacher/edit_teacher.html", {"form": form})
