from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.views.generic import View,TemplateView,ListView,UpdateView
from apps.AdminPanel_App.forms import EditUserPanelForms,AddCourseForm
from apps.Course_app.models import Courses
from apps.Acount_app.models import User,Teacher
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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


class CourseList(ListView):
        model = Courses
        template_name = "AdminPanel_App/course_list.html"
        paginate_by = 3


class AddCourse(View):

    def post(self,request):

        form=AddCourseForm(request.POST,request.FILES)

        if form.is_valid():

            user=request.user
            teacher=Teacher.objects.get(user__id=user.id)
            c=form.save(commit=False)
            c.teacher=teacher
            c.save()

            return redirect("AdminPanel:Course_list")


        return render(request,"AdminPanel_App/add-course.html",{"form":form})


    def get(self,request):
        form=AddCourseForm()


        return render(request,"AdminPanel_App/add-course.html",{"form":form})

class EditCourse(UpdateView):

    model = Courses
    form_class = AddCourseForm
    template_name = "AdminPanel_App/add-course.html"
    success_url = reverse_lazy("AdminPanel:Course_list")


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



