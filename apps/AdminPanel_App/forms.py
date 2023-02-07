from django import forms
from .models import RequestsModel
from apps.Acount_app.models import User,Teacher
from apps.Course_app.models import Courses,CoursesChild,Category
from apps.Blog_App.models import BlogModel
from apps.Message_App.models import MessageModel
from apps.Teacher_app.models import TeachersIncome

class EditUserPanelForms(forms.ModelForm):

    class Meta:
        model=User

        fields=["image","full_name","phone","student_number","bio","instagram","twitter","linkedin","facebook","nation_code"]

        widgets={

            "image":forms.FileInput(
                attrs={
                    "class":"form-control"
                }
            ),
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

            "nation_code":forms.TextInput(
                attrs={
                    "class":"form-control"
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

    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)
        self.fields['phone'].disabled = True
        self.fields['student_number'].disabled = True


class AddCourseForm(forms.ModelForm):

    class Meta:

        model=Courses
        exclude=("view","slug","user")



        widgets={


            "teacher":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),

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

            "how_to_hold": forms.Select(
                attrs={
                    "class": "form-control"
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
            ),

            "capacity":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "start_registration":forms.DateTimeInput(

            attrs={
                "class":"form-control"
            }
            ),

            "end_registration":forms.DateTimeInput(
                attrs={
                    "class":"form-control"
                }
            ),
        }


class AddVideoChildForm(forms.ModelForm):

    class Meta:

        model=CoursesChild
        exclude=["topic_parent","parent"]


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
            ),


        }


class CreateCategoryForm(forms.ModelForm):

    class Meta:
        model=Category

        fields=["name","image"]


        widgets={

            "name":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "image":forms.FileInput(
                attrs={
                    "class":"custom-file-input"
                }
            )
        }


class RequestTeacherForm(forms.ModelForm):

    class Meta:

        model=Teacher
        exclude=("user","status")

        widgets={

            "resume":forms.FileInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "position":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),

            "bio":forms.TextInput(
                attrs={
                    "class":"form-control summernote"
                }
            )
        }


class EditTeacherForm(forms.ModelForm):

    class Meta:

        model=Teacher
        fields="__all__"

        widgets={


            "user":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),



            "resume":forms.FileInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "position":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),

            "bio":forms.TextInput(
                attrs={
                    "class":"form-control summernote"
                }
            )
        }


class RequestsForm(forms.ModelForm):

    class Meta:
        model=RequestsModel
        exclude=("user","is_blogger","is_technical_team")


        widgets={





            "resume":forms.FileInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "position":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),

            "introduction": forms.Textarea(
                attrs={
                    "class":"form-control"
                }
            ),




        }


class RequestsUpdateForm(forms.ModelForm):

    class Meta:
        model=RequestsModel
        exclude=("user",)


        widgets={


            "is_blogger":forms.CheckboxInput(),
            "is_teacher":forms.CheckboxInput(),
            "is_employee":forms.CheckboxInput(),


            "resume":forms.FileInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "position":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),

            "introduction": forms.Textarea(
                attrs={
                    "class":"form-control"
                }
            ),




        }

class CreateBlogForm(forms.ModelForm):


    class Meta:

        model=BlogModel
        exclude=("user","view","created","status")

        widgets={

            "titel":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"عنوان مقاله را وارد کنید"
                }
            ),

            "image":forms.FileInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "text":forms.Textarea(
                attrs={
                    "class":"form-control summernote"
                }
            ),

            "category":forms.SelectMultiple(

                attrs={
                    "class":"form-control"
                }
            ),


        }



class UpdateBlogForm(forms.ModelForm):


    class Meta:

        model=BlogModel
        exclude=("user","view","created")

        widgets={

            "titel":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"عنوان مقاله را وارد کنید"
                }
            ),

            "image":forms.FileInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "text":forms.Textarea(
                attrs={
                    "class":"form-control summernote"
                }
            ),

            "category":forms.SelectMultiple(

                attrs={
                    "class":"form-control"
                }
            ),


        }




class CreateMessageForm(forms.ModelForm):


    class Meta:

        model=MessageModel

        exclude=("created",)


        widgets={
            "courses":forms.CheckboxSelectMultiple()
        }

    # courses=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Courses.objects.all())


class AddAcsess(forms.ModelForm):

    class Meta:

        model=User
        exclude=("password","facebook","twitter","instagram","linkedin")

        widgets={
            "full_name":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "phone":forms.TextInput(attrs={
                "class":"form-control"
            }),

            "email":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "bio":forms.TextInput(
                attrs={
                    "class":"form-control summernote"
                }
            ),

            "student_number":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),

            "university_name":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),

            "major":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),

            "position":forms.Select(

                attrs={
                    "class":"form-control",

                }
            )


        }


class TeacherIncomeForms(forms.ModelForm):

    class Meta:

        model=TeachersIncome
        fields="__all__"

        widgets={
            "teacher":forms.Select(
                attrs={
                    "class":"form-control",
                    'readonly': 'readonly'
                }
            ),

            "course":forms.Select(
                attrs={
                    "class":"form-control",
                }
            ),

            "income":forms.NumberInput(
                attrs={
                    "class":"form-control"
                }
            )
        }




    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)
        self.fields['teacher'].disabled = True
        self.fields['course'].disabled = True
        self.fields['income'].disabled = True