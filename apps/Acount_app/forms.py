from django import forms
from django.db.models import Q
from apps.Acount_app.models import User


UNIVERSITY_NAME = (
    ("دانشگاه صنعتی سیرجان", "دانشگاه صنعتی سیرجان"),
    ("دانشگاه باهنر کرمان", "دانشگاه باهنر کرمان"),
    ("سایر دانشگاه ها", "سایر دانشگاه ها"),
)

MAJOR= (
    ("مهندسی کامپیوتر", "مهندسی کامپیوتر"),
    ("مهندسی برق", "مهندسی برق"),
    ("مهندسی شیمی", "مهندسی شیمی"),
    ("علوم کامپیوتر", "علوم کامپیوتر"),
    ("سایر رشته ها", "سایر رشته ها"),
)


class SignForm(forms.Form):

    phone=forms.CharField(max_length=14,widget=forms.TextInput(
        attrs={
            "class":"form-control"
        }
    ))
    full_name=forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={
            "class":"form-control"
        }
    ))
    student_number=forms.CharField(max_length=50,widget=forms.TextInput(
        attrs={
            "class":"form-control"
        }
    ))
    password1=forms.CharField(max_length=50,widget=forms.PasswordInput(
        attrs={
            "class":"form-control"
        }
    ))
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput(
        attrs={
            "class":"form-control"
        }
    ))

    university_name=forms.ChoiceField(choices=UNIVERSITY_NAME,)
    major=forms.ChoiceField(choices=MAJOR,)



    def clean(self):
        cd=self.cleaned_data

        phone = cd.get("phone")
        student_number = cd.get("student_number")
        password1 = cd.get("password1")
        password2 = cd.get("password2")

        if User.objects.filter(phone=phone).exists():

            raise forms.ValidationError("کاربر با این شماره موبایل در سایت وجود دارد")

        elif User.objects.filter(student_number=student_number).exists():

            raise forms.ValidationError("کاربر با این شماره دانشجویی از قبل در سایت وجود دارد")

        elif password2 != password1 :

            raise forms.ValidationError("پسورد ها باهم مطابقت ندارد!")


class LoginForm(forms.Form):

    phone=forms.CharField(max_length=50,widget=forms.TextInput(
        attrs={
            "class":"form-control"
        }
    ))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(
        attrs={
            "class":"form-control"
        }
    ))


