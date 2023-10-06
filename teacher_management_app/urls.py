from django.urls import path

from teacher_management_app.views import create_teacher, show_teachers, \
    edit_teacher, delete_teacher

urlpatterns = [path("teachers/", show_teachers),
               path("create_teacher/", create_teacher),
               path("edit_teacher/", edit_teacher),
               path("delete_teacher/", delete_teacher)]
