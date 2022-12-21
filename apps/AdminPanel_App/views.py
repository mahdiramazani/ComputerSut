from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.views.generic import View,TemplateView,ListView,UpdateView
from apps.AdminPanel_App.forms import EditUserPanelForms,AddCourseForm,AddVideoChildForm
from apps.Course_app.models import Courses,CoursesChild,Category
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

class AddVideoChild(View):


    def post(self,request,pk):

        form=AddVideoChildForm(request.POST,request.FILES)

        if form.is_valid():
            parent=Courses.objects.get(id=pk)

            v=form.save(commit=False)
            v.parent=parent
            v.save()

            return redirect("/")

        print(form.errors)

        return render(request, "AdminPanel_App/add_video_cuorseChild.html", {"form": form})


    def get(self,request,pk):

        form=AddVideoChildForm()


        return render(request,"AdminPanel_App/add_video_cuorseChild.html",{"form":form})

class VideoChildList(View):

    def get(self,request,pk):

        course_child=CoursesChild.objects.filter(parent_id=pk)

        object_list=Paginator(course_child,1)
        page=request.GET.get("page")

        try:
            page_obj = object_list.get_page(page)
        except PageNotAnInteger:

            page_obj = object_list.page(1)
        except EmptyPage:

            page_obj = object_list.page(object_list.num_pages)

        return render(request,"AdminPanel_App/video_child_list.html",{"course":course_child,"page_obj":page_obj})

class EditVideoChild(UpdateView):
    model = CoursesChild
    form_class = AddVideoChildForm
    template_name = "AdminPanel_App/add_video_cuorseChild.html"
    success_url = "/"


class CategoryCourse(ListView):
    model = Category
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



