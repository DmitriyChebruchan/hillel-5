from django import forms
import phonenumbers
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "surname",
            "year",
            "group",
            "phone_number",
        ]

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        surname = cleaned_data.get("surname")
        phone = self.cleaned_data["phone_number"]

        # phone check
        if not phone:
            raise forms.ValidationError("Phone is missing")

        min_phone_length = 8  # Change to your desired minimum length
        if len(phone) < min_phone_length:
            raise forms.ValidationError("Phone is too short")

        parsed_phone = phonenumbers.parse(phone)
        format = phonenumbers.PhoneNumberFormat.INTERNATIONAL
        phone = phonenumbers.format_number(
            numobj=parsed_phone, num_format=format
        )

        # Check if 'first_name' contains digits
        if any(char.isdigit() for char in first_name):
            self.add_error(
                "first_name",
                "First name should not contain digits.",
            )

        # Check if 'surname' contains digits
        if any(char.isdigit() for char in surname):
            self.add_error(
                "surname",
                "Surname should not contain digits.",
            )


class AddingStudentToGroupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["group"]
