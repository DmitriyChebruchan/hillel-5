from django.urls import path

from student_management_app.views import (
    add_students_to_group,
    create_student,
    edit_student,
    show_students,
)

urlpatterns = [
    path(
        "list_of_students/",
        show_students,
        name="list_of_students",
    ),
    path("create_student/", create_student),
    path(
        "edit_student/<int:pk>",
        edit_student,
        name="edit_student",
    ),
    path(
        "adding_student_to_group/<int:pk>",
        add_students_to_group,
        name="adding_student_to_group",
    ),
]
