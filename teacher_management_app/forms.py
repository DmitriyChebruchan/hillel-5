from django import forms

from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "patronymic", "surname", "age", "subject"]

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        patronymic = cleaned_data.get("patronymic")
        surname = cleaned_data.get("surname")
        subject = cleaned_data.get("subject")

        # Check if 'first_name' contains digits
        if any(char.isdigit() for char in first_name):
            self.add_error("first_name", "First name should not contain digits.")

        # Check if 'patronymic' contains digits
        if any(char.isdigit() for char in patronymic):
            self.add_error("patronymic", "Patronymic should not contain digits.")

        # Check if 'surname' contains digits
        if any(char.isdigit() for char in surname):
            self.add_error("surname", "Surname should not contain digits.")

        # Check if 'subject' contains digits
        if any(char.isdigit() for char in subject):
            self.add_error("subject", "Subject should not contain digits.")
