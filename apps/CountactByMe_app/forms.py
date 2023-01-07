from django import forms
from .models import ContactUs



class CountactUsForm(forms.ModelForm):



    class Meta:

        model=ContactUs

        exclude=("created",)

        widgets={
            "full_name":forms.TextInput(
                attrs={
                    "class":"form-control",
                }
            ),

            "phone_number":forms.TextInput(

                attrs={
                    "class":"form-control"
                }
            ),

            "body":forms.Textarea(
                attrs={
                    "class":"form-control"
                }
            )
        }


