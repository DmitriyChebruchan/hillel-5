from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "surname", "year", "group"]

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        surname = cleaned_data.get("surname")

        # Check if 'first_name' contains digits
        if any(char.isdigit() for char in first_name):
            self.add_error("first_name",
                           "First name should not contain digits.")

        # Check if 'surname' contains digits
        if any(char.isdigit() for char in surname):
            self.add_error("surname", "Surname should not contain digits.")


class AddingStudentToGroupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["group"]
