from django.shortcuts import redirect, render

from group_management_app.models import Group

from .forms import GroupForm


def show_groups(request):
    all_groups = Group.objects.all()
    return render(request, "group/list_of_groups.html", {"data": all_groups})


def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/groups/")

    else:
        if request.method == "GET":
            form = GroupForm()

    return render(request, "group/group_form.html", {"form": form})
