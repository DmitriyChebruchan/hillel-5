from django.urls import path

from group_management_app.views import (
    create_group,
    show_groups,
)

urlpatterns = [
    path("groups/", show_groups),
    path("create_group/", create_group),
]
