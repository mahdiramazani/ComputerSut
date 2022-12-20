from django import forms
from apps.Acount_app.models import User,Teacher



class EditUserPanelForms(forms.ModelForm):

    class Meta:
        model=User

        fields=["full_name","phone","student_number","bio","instagram","twitter","linkedin","facebook"]

        widgets={
            "full_name":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"نام و نام خانواگی"
                }
            ),

            "phone":forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"َشماره تلفن"
                }
            ),

            "student_number":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"شماره دانشجویی"
                }
            ),

            "bio":forms.Textarea(
                attrs={
                    "class":"form-control summernote",
                    "placeholder":"بیوگرافی"
                }
            ),

            "instagram":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"لینک اینستاگرام"
                }
            ),

            "linkedin":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"لینک لینکدین"
                }
            ),

            "twitter":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"لینک توییتر"
                }
            ),

            "facebook":forms.TextInput(

                attrs={
                    "class":"form-control",
                    "placeholder":"لینک فیسبوک"
                }
            )
        }

