from django.urls import path

from teacher_management_app.views import (create_teacher, edit_teacher,
                                          show_teachers)

urlpatterns = [
    path("list_of_teachers/", show_teachers, name="list_of_teachers"),
    path("create_teacher/", create_teacher),
    path("edit_teacher/<int:pk>", edit_teacher, name="edit_teacher"),
]
