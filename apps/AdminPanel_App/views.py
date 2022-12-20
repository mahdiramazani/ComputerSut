from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from apps.AdminPanel_App.forms import EditUserPanelForms
from apps.Course_app.models import Courses

class AdminPanelView(View):

    def post(self, request):
        form = EditUserPanelForms(request.POST,request.FILES,instance=request.user)

        if form.is_valid():
            form.save()

            return render(request, "AdminPanel_App/user_panel.html",{"form":form})

        return render(request, "AdminPanel_App/user_panel.html",{"form":form})

    def get(self, request):

        form=EditUserPanelForms(instance=request.user)

        return render(request, "AdminPanel_App/user_panel.html",{"form":form})


class DashboardView(TemplateView):

    template_name = "AdminPanel_App/dashboard.html"


class CourseList(View):




    def get(self,request):

        course=Courses.objects.all()


        return render(request,"AdminPanel_App/course_list.html",{"course":course})


class AddCourse(TemplateView):

    template_name = "AdminPanel_App/add-course.html"


class CategoryCourse(TemplateView):

    template_name = "AdminPanel_App/course-category.html"


class Coupons(TemplateView):

    template_name = "AdminPanel_App/coupons.html"

class RegisterStudent(TemplateView):
    template_name = "AdminPanel_App/register_student.html"


class AdminList(TemplateView):

    template_name = "AdminPanel_App/kist-admins.html"


class AddAdmin(TemplateView):

    template_name = "AdminPanel_App/add-admin.html"


class AddTeacher(TemplateView):

    template_name = "AdminPanel_App/add-teacher.html"

class TeacherList(TemplateView):

    template_name = "AdminPanel_App/list_teacher.html"


class StudentList(TemplateView):

    template_name = "AdminPanel_App/student_list.html"


class AddStudent(TemplateView):

    template_name = "AdminPanel_App/add-students.html"



