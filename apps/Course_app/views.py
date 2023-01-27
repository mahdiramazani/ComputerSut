from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, View
from apps.Course_app.models import Courses, CoursesChild, Category, Comment,Checkout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CategoryCourse(View):

    def get(self,request,id):
        category=Category.objects.get(id=id)

        course=category.Corses.all()

        paginator = Paginator(course, 6)
        page = request.GET.get("page")

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        return render(request, "Course_app/course.html", {"object_list": object_list})

class CoursesView(View):
    model = Courses
    template_name = "Course_app/course.html"

    def get(self, request):

        object_list = Courses.objects.all()

        paginator = Paginator(object_list,6)
        page = request.GET.get("page")

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        return render(request, "Course_app/course.html", {"object_list": object_list})


class CourseDetailView(View):

    def get(self, request, pk):
        context = {"student": False}

        object = Courses.objects.get(id=pk)

        object.view+=1

        object.save()
        context["object"]=object
        context["last_course"]=Courses.objects.all()[0:3]


        if request.user in object.user.all():

            context["student"] = True

        return render(request, "Course_app/course-detail.html", {"object": context})



    def post(self, request, pk):

        curses = Courses.objects.get(id=pk)
        body = request.POST.get("body")

        if request.user not in curses.user.all():

            # curses.user.add(request.user)
            # curses.save()
            user=request.user
            course=Courses.objects.get(id=pk)
            price=(course.price)


            if not Checkout.objects.filter(user=user,course=course).exists():

                Checkout.objects.create(user=user,course=course,price=price)

        if body is not None:

            Comment.objects.create(user=request.user, body=body, corses=curses)

        return redirect(reverse("Course_app:Course_detail", kwargs={"pk": pk}))


class CourseDetailVideoView(DetailView):
    model = CoursesChild

    template_name = "Course_app/course_video_detail.html"


class CheckOutClass(TemplateView):

    template_name = "Course_app/checkout.html"