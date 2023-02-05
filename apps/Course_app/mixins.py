from apps.Acount_app.models import User, Teacher
from apps.Course_app.models import Courses, CoursesChild
from django.shortcuts import redirect
from apps.Course_app.models import Checkout


class CheckCapcityMixin:

    def dispatch(self, request, pk):

        course = Courses.objects.get(id=pk)

        if course.how_to_hold == "حضوری":

            if course.capacity >= 1:

                if course.registration_time():

                    return super().dispatch(request, pk)

                else:
                    return redirect(course.get_absulot_url())
            else:
                return redirect(course.get_absulot_url())

        else:

            return super().dispatch(request, pk)


class CheckStudentCourseMixin:

    def dispatch(self, request, pk):
        course_child = CoursesChild.objects.get(id=pk)
        course = course_child.parent

        if request.user.is_authenticated:

            user = request.user
            teacher = Teacher.objects.get(user=user)

            if user in course.user.all() or user.is_admin == True or course.teacher == teacher:

                return super(CheckStudentCourseMixin, self).dispatch(request, pk)

            else:

                return redirect(course.get_absulot_url())

        else:

            return redirect(course.get_absulot_url())


class CheckLoginMixin:

    def dispatch(self, request):
        if request.user.is_authenticated:
            return super(CheckLoginMixin, self).dispatch(request)

        return redirect("Home_app:Home")


class CheckOrderShopMixin:

    def dispatch(self, request):

        if request.user.is_authenticated:
            pk = request.GET.get("checkout_id")

            user = request.user

            if Checkout.objects.filter(id=pk, user=user).exists():

                return super().dispatch(request)

            else:

                return redirect("Home_app:Home")
        else:
            return redirect("Home_app:Home")


class CheckRequestToPayMixin:

    def dispatch(self, request, pk):

        if request.user.is_authenticated:

            if Checkout.objects.filter(id=pk, user=request.user, is_paid=False).exists():

                checkout = Checkout.objects.get(id=pk)

                if checkout.course.how_to_hold == "حضوری":

                    if checkout.course.capacity >= 1:

                        if checkout.course.registration_time():

                            return super().dispatch(request, pk)

                        else:

                            return redirect(checkout.course.get_absulot_url())
                    else:

                        return redirect(checkout.course.get_absulot_url())
                else:

                    return super().dispatch(request, pk)

            else:

                return redirect("Home_app:Home")

        else:

            return redirect("Home_app:Home")


class VidoChildMixin:

    def dispatch(self, request, pk):

        video_child = CoursesChild.objects.get(id=pk)

        if video_child.parent.how_to_hold == "حضوری":

            if video_child.lock == False:

                return super(VidoChildMixin, self).dispatch(request, pk)

            else:

                if request.user.is_authenticated:
                    user = request.user
                    teacher = video_child.parent.teacher

                    if (user.is_admin == True) or (user.is_employee == True) or (teacher.user == user) or (
                            user in video_child.parent.user.all()):
                        return super(VidoChildMixin, self).dispatch(request, pk)

                else:
                    return redirect(video_child.parent.get_absulot_url())
        else:

            if request.user.is_authenticated:

                user = request.user
                teacher = video_child.parent.teacher

                if (user.is_admin == True) or (user.is_employee == True) or (teacher.user == user) or (
                        user in video_child.parent.user.all()):

                    return super(VidoChildMixin, self).dispatch(request, pk)

                else:

                    return redirect(video_child.parent.get_absulot_url())

            else:
                return redirect(video_child.parent.get_absulot_url())
