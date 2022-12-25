from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView
from apps.AdminPanel_App.forms import EditUserPanelForms, AddCourseForm, AddVideoChildForm, CreateCategoryForm, \
    RequestTeacherForm, EditTeacherForm,RequestsForm,RequestsUpdateForm,CreateBlogForm
from apps.Course_app.models import Courses, CoursesChild, Category,CertificatesOfCourses
from apps.Acount_app.models import User, Teacher
from apps.Acount_app.forms import SignForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.AdminPanel_App.mixins import CheckTeacherMixin,CheckAdmin,CheckIsTeacherMixin
from .models import RequestsModel
from apps.Blog_App.models import Category,BlogModel

class AdminPanelView(View):

    def post(self, request):
        form = EditUserPanelForms(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()

            return render(request, "AdminPanel_App/user_panel.html", {"form": form})

        return render(request, "AdminPanel_App/user_panel.html", {"form": form})

    def get(self, request):
        form = EditUserPanelForms(instance=request.user)

        return render(request, "AdminPanel_App/user_panel.html", {"form": form})


class DashboardView(TemplateView):
    template_name = "AdminPanel_App/dashboard.html"


class CourseList(CheckTeacherMixin,ListView):
    model = Courses
    template_name = "AdminPanel_App/course_list.html"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_admin == True:

            return qs

        else:
            user=self.request.user
            teacher=Teacher.objects.get(user=user)
            qs=super().get_queryset()

            return qs.filter(teacher=teacher)


class Students_Of_The_Course(CheckIsTeacherMixin,View):

    def get(self,request,pk):

        course=Courses.objects.get(id=pk)
        users=course.user.all()

        return render(request,"AdminPanel_App/student_list.html",{"users":users})


class AddCourse(CheckTeacherMixin,View):

    def post(self, request):
        form = AddCourseForm(request.POST, request.FILES)

        if form.is_valid():
            user = request.user
            teacher = Teacher.objects.get(user__id=user.id)
            c = form.save(commit=False)
            c.teacher = teacher
            c.save()

            return redirect("AdminPanel:Course_list")

        return render(request, "AdminPanel_App/add-course.html", {"form": form})

    def get(self, request):
        form = AddCourseForm()

        return render(request, "AdminPanel_App/add-course.html", {"form": form})


class EditCourse(CheckIsTeacherMixin,UpdateView):
    model = Courses
    form_class = AddCourseForm
    template_name = "AdminPanel_App/add-course.html"
    success_url = reverse_lazy("AdminPanel:Course_list")


class AddVideoChild(CheckIsTeacherMixin,View):

    def post(self, request, pk):
        form = AddVideoChildForm(request.POST, request.FILES)

        if form.is_valid():
            parent = Courses.objects.get(id=pk)

            v = form.save(commit=False)
            v.parent = parent
            v.save()

            return redirect("/")

        print(form.errors)

        return render(request, "AdminPanel_App/add_video_cuorseChild.html", {"form": form})

    def get(self, request, pk):
        form = AddVideoChildForm()

        return render(request, "AdminPanel_App/add_video_cuorseChild.html", {"form": form})


class VideoChildList(CheckIsTeacherMixin,View):

    def get(self, request, pk):

        course_child = CoursesChild.objects.filter(parent_id=pk)

        object_list = Paginator(course_child, 1)
        page = request.GET.get("page")

        try:
            page_obj = object_list.get_page(page)
        except PageNotAnInteger:

            page_obj = object_list.page(1)
        except EmptyPage:

            page_obj = object_list.page(object_list.num_pages)

        return render(request, "AdminPanel_App/video_child_list.html", {"course": course_child, "page_obj": page_obj})


class EditVideoChild(CheckIsTeacherMixin,UpdateView):
    model = CoursesChild
    form_class = AddVideoChildForm
    template_name = "AdminPanel_App/add_video_cuorseChild.html"
    success_url = "/"


class CategoryCourse(CheckAdmin,ListView):
    model = Category
    template_name = "AdminPanel_App/course-category.html"


class CreateCategoryView(CheckAdmin,CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = "AdminPanel_App/create_category.html"
    success_url = reverse_lazy("AdminPanel:Category_course")


class EditCategory(CheckAdmin,UpdateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = "AdminPanel_App/create_category.html"
    success_url = reverse_lazy("AdminPanel:Category_course")


class Coupons(CheckAdmin,TemplateView):
    template_name = "AdminPanel_App/coupons.html"


class CertificatesOfCoursesView(CheckTeacherMixin,View):


    def post(self,request):
        user = request.user
        teacher = Teacher.objects.get(user=user)
        course = Courses.objects.get(teacher=teacher)

        student=request.POST.get("student")
        courses=request.POST.get("course")
        document=request.FILES.get("document")
        student_user=User.objects.get(student_number=student)

        if User.objects.filter(id=user.id).exists():

            if Courses.objects.filter(user=student_user).exists():
                c=Courses.objects.get(id=courses)

                CertificatesOfCourses.objects.create(user=student_user,course=c,document=document)

                return redirect("/")

        return render(request, "AdminPanel_App/madrak.html", {"course": course})


    def get(self,request):

        user=request.user

        if request.user.is_admin == True:
            course = Courses.objects.all()

        else:
            teacher=Teacher.objects.get(user=user)
            course=Courses.objects.filter(teacher=teacher)

        return render(request,"AdminPanel_App/madrak.html",{"course":course})


class RegisterStudent(CheckAdmin,View):

    def post(self, request):
        form = SignForm(request.POST, request.FILES)

        if form.is_valid():
            cd = form.cleaned_data
            phone = cd.get("phone")
            full_name = cd.get("full_name")
            student_number = cd.get("student_number")
            password1 = cd.get("password1")
            password2 = cd.get("password2")
            university_name = cd.get("university_name")
            major = cd.get("major")

            user = User.objects.create(phone=phone, full_name=full_name, student_number=student_number,
                                       password=password1, university_name=university_name, major=major)

            user.set_password(password1)
            user.save()

            return redirect("/")

        return render(request, "AdminPanel_App/add-students.html", {"form": form})

    def get(self, request):
        form = SignForm()

        return render(request, "AdminPanel_App/add-students.html", {"form": form})


class RequestToTeacherView(View):

    def post(self, request):
        form = RequestTeacherForm(request.POST, request.FILES)

        user = request.user
        teacher = Teacher.objects.filter(user=user).exists()

        if not teacher:
            if form.is_valid():
                user = request.user

                t = form.save(commit=False)

                t.user = user
                t.save()

                return redirect("/")

        return render(request, "AdminPanel_App/request_to_teacher.html", {"form": form})

    def get(self, request):

        form = RequestTeacherForm()

        user = request.user
        if Teacher.objects.filter(user=user, status=False).exists():
            t = False

            return render(request, "AdminPanel_App/request_to_teacher.html", {"form": form, "teacher": t})


        elif Teacher.objects.filter(user=user, status=True).exists():

            t = True
            return render(request, "AdminPanel_App/request_to_teacher.html", {"form": form, "teacher": t})

        return render(request, "AdminPanel_App/request_to_teacher.html", {"form": form})


class TeacherList(CheckAdmin,ListView):
    template_name = "AdminPanel_App/list_teacher.html"
    model = Teacher
    paginate_by = 10


class EditTeacherView(CheckAdmin,View):



    def post(self,request,pk):
        teacher = Teacher.objects.get(id=pk)
        form=EditTeacherForm(request.POST,request.FILES,instance=teacher)

        if form.is_valid():

            form.save()

            user = teacher.user
            if teacher.status == True:
                u = User.objects.get(id=user.id)
                u.is_teacher = True
                u.save()

            elif teacher.status == False:

                u = User.objects.get(id=user.id)
                u.is_teacher = False
                u.save()


            return redirect("AdminPanel:Teacher_list")


        return render(request, "AdminPanel_App/edit_teacher.html", {"form": form})

    def get(self,request,pk):
        teacher = Teacher.objects.get(id=pk)
        form=EditTeacherForm(instance=teacher)



        return render(request,"AdminPanel_App/edit_teacher.html",{"form":form})


class AdminList(CheckAdmin,TemplateView):
    template_name = "AdminPanel_App/kist-admins.html"


class AddAdmin(CheckAdmin,TemplateView):
    template_name = "AdminPanel_App/add-admin.html"


class AddTeacher(CheckAdmin,TemplateView):
    template_name = "AdminPanel_App/add-teacher.html"


class StudentList(View):

    def get(self,request):
        u=User.objects.all()
        us=Paginator(u,1)
        page=request.GET.get("page")
        users= us.get_page(page)

        return render(request,"AdminPanel_App/student_list.html",{"users":users})


class AddStudent(CheckAdmin,View):

    def post(self, request):
        context = {}
        courses = Courses.objects.all()
        context["course"] = courses

        user = request.POST.get("user")
        id = request.POST.get("course")

        student=User.objects.get(student_number=user)
        course=Courses.objects.get(id=id)

        course.user.add(student)



        return render(request, "AdminPanel_App/register_student.html",context=context)

    def get(self, request):
        context = {}
        courses = Courses.objects.all()
        context["course"] = courses

        return render(request, "AdminPanel_App/register_student.html", context=context)


class MyDocumentsView(ListView):

    model = CertificatesOfCourses
    template_name ="AdminPanel_App/my_doucument.html"

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()

        if user.is_admin:

            return qs

        else:

            return qs.filter(user=user)


class RequestsView(View):

    def post(self,request):

        form=RequestsForm(request.POST,request.FILES)

        if form.is_valid():

            user=request.user

            f=form.save(commit=False)
            f.user=user
            f.save()

            return redirect(reverse("AdminPanel:Userpanel"))

        print(form.errors)

        return render(request, "AdminPanel_App/requests.html",{"form":form})

    def get(self,request):

        form=RequestsForm()

        return render(request,"AdminPanel_App/requests.html",{"form":form})


class RequestListView(ListView):

    model=RequestsModel
    template_name = "AdminPanel_App/request_list.html"
    paginate_by = 10


class RequestListUpdate(View):


    def post(self,request,pk):
        req = RequestsModel.objects.get(id=pk)
        form = RequestsUpdateForm(request.POST, request.FILES, instance=req)
        user=User.objects.get(id=req.user.id)

        if form.is_valid():

            form.save()

            if req.is_blogger == True:

                user.is_blogger = True

            else:
                user.is_blogger = False


            if req.is_technical_team == True:

                user.is_technical_team = True

            else:
                user.is_technical_team = False

            user.save()
            return redirect("AdminPanel:request_list")

        return render(request, "AdminPanel_App/requests.html", {"form": form})


    def get(self,request,pk):

        req=RequestsModel.objects.get(id=pk)
        form=RequestsUpdateForm(instance=req)


        return render(request,"AdminPanel_App/requests.html",{"form":form})

class BlogListView(ListView):
    model = BlogModel
    template_name = "AdminPanel_App/blog_list.html"
    paginate_by = 1


class CreateBlogView(View):



    def post(self,request):
        form=CreateBlogForm(request.POST,request.FILES)

        if form.is_valid():
            user=request.user
            b=form.save(commit=False)
            b.user=user
            b.save()

            return redirect(reverse("AdminPanel:blog_list"))


        return render(request,"AdminPanel_App/create_blog.html",{"form":form})


    def get(self,request):

        form=CreateBlogForm()


        return render(request,"AdminPanel_App/create_blog.html",{"form":form})


class UpdateBlogView(UpdateView):

    model = BlogModel
    template_name = "AdminPanel_App/create_blog.html"
    form_class = CreateBlogForm
    success_url = reverse_lazy("AdminPanel:blog_list")