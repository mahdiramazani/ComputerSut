from django import forms
from apps.Acount_app.models import User,Teacher
from apps.Course_app.models import Courses,CoursesChild



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

class AddCourseForm(forms.ModelForm):

    class Meta:

        model=Courses
        exclude=("view","user","slug","teacher")



        widgets={




            "titel":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"عنوان دوره را وارد کنید(آموزش مقدماتی سی پلاس پلاس)"
                }
            ),

            "specifications":forms.Textarea(
                attrs={
                    "class":"form-control summernote",
                    "placeholder":"مشخصات فنی دوره را وارد کنید"
                }
            ),
            "Introduction_of_the_valley":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"توضیح خلاصه درباره دوره:برگزار کندده انجمن کامپیوتر سیرجان"
                }
            ),

            "category":forms.SelectMultiple(
                attrs={
                    "class":"form-select",
                    "size":3
                }
            ),

            "level":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),

            "status":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),

            "price":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"قیمت دوره را وارد کنید:"
                }
            ),

            "discount":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"قیمت پس از تخفیف را وارد کنید"
                }
            ),

            "cover":forms.FileInput(
                attrs={
                    "class":"custom-file-input"
                }
            ),

            "introduction_video":forms.FileInput(
                attrs={
                    "class":"custom-file-input"
                }
            ),

            "project_count":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"تعداد پروژه هایی که در این دوره انجام میشود."
                }
            )
        }


class AddVideoChildForm(forms.ModelForm):

    class Meta:

        model=CoursesChild
        exclude=["topic_parent"]


        widgets={



            "introduction":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "video":forms.FileInput(

                attrs={
                    "class":"custom-file-input"
                }
            ),

            "video_cover":forms.FileInput(
                attrs={
                    "class":"custom-file-input"
                }
            ),

            "link_video":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "time":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "topic":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            )
        }