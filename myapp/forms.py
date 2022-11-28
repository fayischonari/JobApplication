
from django import forms
from django.forms import ValidationError
from .models import FormDetails
from django import forms
import re


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = FormDetails
        fields = "__all__"

        # html attributes
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input", "id": "name", "onblur": "validatename()"}
            ),
            "email": forms.TextInput(
                attrs={"class": "input", "id": "email", "onblur": "Validateemail()"}
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "input",
                    "id": "phone",
                    "onblur": "validatephone()",
                    
                }
            ),
            "address": forms.Textarea(attrs={"class": "input", "id": "address"}),
            "dob": forms.TextInput(
                attrs={
                    "class": "input",
                    "id": "dob",
                    "onfocus": '(this.type="date")',
                    "oninput": "validateage()",
                }
            ),
            "gender": forms.RadioSelect(
                attrs={"class": "", "id": "female", "value": "F"}
            ),
            
            "jobrole": forms.Select(attrs={"class": "input", "id": "job"}),
            "experience": forms.Select(attrs={"class": "input", "id": "job"}),
            "linkedin": forms.TextInput(attrs={"class": "input", "id": "name"}),
        }


    def clean_phone(self):
        phone=str(self.cleaned_data["phone"])
        pattern=re.compile(r"(0|91)?[-\s]?[6-9][0-9]{9}")

        if not pattern.match(phone):
            raise ValidationError("Invalid format")
        return phone
        

        
