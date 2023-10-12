from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.urls import reverse

from student_management_app.models import Student

from .forms import AddingStudentToGroupForm, StudentForm


def show_students(request):
    all_students = Student.objects.all()
    return render(
        request,
        "student/list_of_students.html",
        {"data": all_students},
    )


def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/list_of_students/")

    else:
        if request.method == "GET":
            form = StudentForm()

    return render(request, "student/student_form.html", {"form": form})


def edit_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "GET":
        form = StudentForm(instance=student)
        return render(
            request,
            "student/edit_student.html",
            {"form": form},
        )

    form = StudentForm(request.POST, instance=student)

    if "delete" in request.POST:
        student.delete()
        return redirect("list_of_students")

    if form.is_valid():
        form.save()
        return redirect(reverse("list_of_students"))

    return render(request, "student/edit_student.html", {"form": form})


def add_students_to_group(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = AddingStudentToGroupForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list_of_students")
    else:
        form = AddingStudentToGroupForm(instance=student)

    return render(
        request,
        "student/add_group_to_student.html",
        {"form": form, "student": student},
    )
