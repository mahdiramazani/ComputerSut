from apps.Acount_app.models import User, Teacher
from django.shortcuts import redirect
from apps.Course_app.models import Courses, CoursesChild, Checkout


class CheckTeacherMixin:


    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            user = request.user

            if (user.is_teacher == True) or (user.is_admin == True) or (user.is_employee == True):

                if ((user.is_admin == True) or (user.is_employee == True)):

                    return super().dispatch(request, *args, **kwargs)
                else:
                    teacher=Teacher.objects.get(user=user)

                    if teacher.status == True:
                        return super().dispatch(request, *args, **kwargs)
                    else:
                        return redirect("Home_app:Home")


            else:

                return redirect("Home_app:Home")
        else:
            return redirect("Home_app:Home")

class CheckIsTeacherMixin:

    def dispatch(self, request, pk):
        user = request.user

        if request.user.is_authenticated:

            if (user.is_teacher == True) or (user.is_admin == True) or (user.is_employee == True):

                if user.is_admin == True or user.is_employee:

                    return super().dispatch(request, pk)

                else:

                    teacher = Teacher.objects.get(user=user)

                    if teacher.status == True:

                        course = Courses.objects.filter(id=pk).exists()
                        course_child = CoursesChild.objects.filter(id=pk).exists()

                        if course:

                            c = Courses.objects.get(id=pk)

                            if c.teacher == teacher:

                                return super().dispatch(request, pk)

                            else:

                                return redirect("Home_app:Home")

                        elif course_child:

                            c = CoursesChild.objects.get(id=pk)

                            if c.parent.teacher == teacher:
                                return super().dispatch(request, pk)
                        else:

                            return redirect("Home_app:Home")

                    else:
                        return redirect("Home_app:Home")
            else:
                return redirect("Home_app:Home")
        else:
            return redirect("Home_app:Home")

class CheckAdmin:

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_admin == True:

            return super().dispatch(request, *args, **kwargs)

        else:

            return redirect("Home_app:Home")


class AdminEmployeMixin:

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            user = request.user

            if user.is_admin or user.is_employee:

                return super().dispatch(request, *args, **kwargs)

            else:

                return redirect("Home_app:Home")

        else:

            return redirect("Home_app:Home")


class CheckLoginMixin:

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            return super(CheckLoginMixin, self).dispatch(request,*args,**kwargs)
        else:
            return redirect("Home_app:Home")


class CheckBloggerMixin:

    def dispatch(self, request, *args, **kwargs):

        user = request.user

        if user.is_authenticated:

            if user.is_admin or user.is_employee or user.is_blogger:

                return super(CheckBloggerMixin, self).dispatch(request,*args,**kwargs)
            else:
                return redirect("Home_app:Home")

        else:

            return redirect("Home_app:Home")
