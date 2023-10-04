from django import forms

from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "curator"]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get('first_name')

    #     # Check if 'first_name' contains digits
    #     if any(char.isdigit() for char in name):
    #         self.add_error(
    #             'name', 'Name should not contain digits.')
