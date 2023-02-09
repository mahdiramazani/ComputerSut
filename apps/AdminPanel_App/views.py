from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from apps.AdminPanel_App.forms import EditUserPanelForms, AddCourseForm, AddVideoChildForm, CreateCategoryForm, \
    RequestTeacherForm, EditTeacherForm, RequestsForm, RequestsUpdateForm, CreateBlogForm, CreateMessageForm, AddAcsess, \
    TeacherIncomeForms, UpdateBlogForm
from apps.Course_app.models import Courses, CoursesChild, Category, CertificatesOfCourses, Checkout
from apps.Acount_app.models import User, Teacher
from apps.Acount_app.forms import SignForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.AdminPanel_App.mixins import CheckTeacherMixin, CheckAdmin, CheckIsTeacherMixin, AdminEmployeMixin, \
    CheckLoginMixin, CheckBloggerMixin
from apps.Blog_App.models import Category, BlogModel
from apps.Teacher_app.models import TeachersIncome
from django.db.models import Q


class AdminPanelView(CheckLoginMixin, View):

    def post(self, request):
        form = EditUserPanelForms(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()

            return render(request, "AdminPanel_App/user_panel.html", {"form": form})

        return render(request, "AdminPanel_App/user_panel.html", {"form": form})

    def get(self, request):
        form = EditUserPanelForms(instance=request.user)

        return render(request, "AdminPanel_App/user_panel.html", {"form": form})


class DashboardView(CheckLoginMixin, TemplateView):
    template_name = "AdminPanel_App/dashboard.html"


class CourseList(CheckTeacherMixin, ListView):
    model = Courses
    template_name = "AdminPanel_App/course_list.html"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_admin == True:

            return qs

        else:
            user = self.request.user
            teacher = Teacher.objects.get(user=user)
            qs = super().get_queryset()

            return qs.filter(teacher=teacher)


class Students_Of_The_Course(CheckIsTeacherMixin, View):

    def get(self, request, pk):
        course = Courses.objects.get(id=pk)
        users = course.user.all()

        return render(request, "AdminPanel_App/student_list.html", {"users": users})


class AddCourse(AdminEmployeMixin, View):

    def post(self, request):
        form = AddCourseForm(request.POST, request.FILES)

        if form.is_valid():
            # user = request.user
            # teacher = Teacher.objects.get(user__id=user.id)
            # c = form.save(commit=False)
            # c.teacher = teacher
            # c.save()
            form.save()

            return redirect("AdminPanel:Course_list")

        return render(request, "AdminPanel_App/add-course.html", {"form": form})

    def get(self, request):
        form = AddCourseForm()

        return render(request, "AdminPanel_App/add-course.html", {"form": form})


class EditCourse(AdminEmployeMixin, UpdateView):
    model = Courses
    form_class = AddCourseForm
    template_name = "AdminPanel_App/add-course.html"
    success_url = reverse_lazy("AdminPanel:Course_list")


class AddVideoChild(CheckIsTeacherMixin, View):

    def post(self, request, pk):
        form = AddVideoChildForm(request.POST, request.FILES)

        if form.is_valid():
            parent = Courses.objects.get(id=pk)

            v = form.save(commit=False)
            v.parent = parent
            v.save()

            return redirect(reverse("AdminPanel:video_child_list",kwargs={"pk":pk}))



        return render(request, "AdminPanel_App/add_video_cuorseChild.html", {"form": form})

    def get(self, request, pk):
        form = AddVideoChildForm()

        return render(request, "AdminPanel_App/add_video_cuorseChild.html", {"form": form})


class VideoChildList(CheckIsTeacherMixin, View):

    def get(self, request, pk):

        course_child = CoursesChild.objects.filter(parent_id=pk)

        object_list = Paginator(course_child, 10)
        page = request.GET.get("page")

        try:
            page_obj = object_list.get_page(page)
        except PageNotAnInteger:

            page_obj = object_list.page(1)
        except EmptyPage:

            page_obj = object_list.page(object_list.num_pages)

        return render(request, "AdminPanel_App/video_child_list.html", {"course": course_child, "page_obj": page_obj})


class EditVideoChild(CheckIsTeacherMixin, UpdateView):
    model = CoursesChild
    form_class = AddVideoChildForm
    template_name = "AdminPanel_App/add_video_cuorseChild.html"

    def get_success_url(self):

        video_child=CoursesChild.objects.get(id=self.object.pk)

        return reverse("AdminPanel:video_child_list",kwargs={"pk":video_child.parent.id})


class CategoryCourse(AdminEmployeMixin, ListView):
    model = Category
    template_name = "AdminPanel_App/course-category.html"


class CreateCategoryView(AdminEmployeMixin, CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = "AdminPanel_App/create_category.html"
    success_url = reverse_lazy("AdminPanel:Category_course")


class EditCategory(AdminEmployeMixin, UpdateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = "AdminPanel_App/create_category.html"
    success_url = reverse_lazy("AdminPanel:Category_course")


class Coupons(AdminEmployeMixin, TemplateView):
    template_name = "AdminPanel_App/coupons.html"


class CertificatesOfCoursesView(CheckTeacherMixin, View):

    def post(self, request):
        context={"errors":[]}
        user = request.user
        teacher = Teacher.objects.get(user=user)
        course = Courses.objects.filter(teacher=teacher)

        student = request.POST.get("student")
        courses = request.POST.get("course")
        document = request.FILES.get("document")
        document_number = request.POST.get("document_number")
        image_document = request.FILES.get("image_document")
        c = Courses.objects.get(id=courses)


        if User.objects.filter(student_number=student).exists():

            student_user=User.objects.get(student_number=student)

            if student_user in c.user.all():

                if not CertificatesOfCourses.objects.filter(document_number=document_number).exists():




                    CertificatesOfCourses.objects.create(user=student_user, course=c, document=document,
                                                        document_number=document_number,image_document=image_document)

                    context["errors"].append("مدرک با موفقیت صادر شد")
                    return render(request, "AdminPanel_App/madrak.html",
                                  {"course": course, "context": context["errors"]})

                else:
                    context["errors"].append("شماره مدرک تکراری است")
                    return render(request, "AdminPanel_App/madrak.html",
                                  {"course": course, "context": context["errors"]})

            else:
                context["errors"].append("این کاربر دانشجوی دوره نمی باشد")
                return render(request, "AdminPanel_App/madrak.html", {"course": course, "context": context["errors"]})
        else:
            context["errors"].append("کاربری با این شماره دانشجویی در سایت وجود ندارد")
            return render(request, "AdminPanel_App/madrak.html", {"course": course, "context": context["errors"]})




    def get(self, request):

        user = request.user

        if request.user.is_admin == True:
            course = Courses.objects.all()

        else:
            teacher = Teacher.objects.get(user=user)
            course = Courses.objects.filter(teacher=teacher)

        return render(request, "AdminPanel_App/madrak.html", {"course": course})


class RegisterStudent(CheckAdmin, View):

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


class RequestToTeacherView(CheckLoginMixin, View):

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

                return redirect("AdminPanel:Request_Teacher")

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


class TeacherList(AdminEmployeMixin, ListView):
    template_name = "AdminPanel_App/list_teacher.html"
    model = Teacher
    paginate_by = 10


class EditTeacherView(AdminEmployeMixin, View):

    def post(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        form = EditTeacherForm(request.POST, request.FILES, instance=teacher)

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

    def get(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        form = EditTeacherForm(instance=teacher)

        return render(request, "AdminPanel_App/edit_teacher.html", {"form": form})


class AdminList(CheckAdmin, ListView):
    template_name = "AdminPanel_App/kist-admins.html"

    paginate_by = 10

    def get_queryset(self):
        qs = User.objects.filter(
            Q(is_admin=True) | Q(is_teacher=True) | Q(is_technical_team=True) | Q(is_employee=True))

        return qs


class AddAdmin(CheckAdmin, TemplateView):
    template_name = "AdminPanel_App/add-admin.html"


class AddTeacher(CheckAdmin, TemplateView):
    template_name = "AdminPanel_App/add-teacher.html"


class StudentList(AdminEmployeMixin, View):

    def get(self, request):
        u = User.objects.all()
        us = Paginator(u, 20)
        page = request.GET.get("page")
        users = us.get_page(page)

        return render(request, "AdminPanel_App/student_list.html", {"users": users})


class AddStudent(CheckAdmin, View):

    def post(self, request):
        context = {"errors":[],}
        courses = Courses.objects.all()
        context["course"] = courses

        user = request.POST.get("user")
        id = request.POST.get("course")

        if User.objects.filter(student_number=user).exists():


            student = User.objects.get(student_number=user)
            course = Courses.objects.get(id=id)

            if student not in course.user.all():

                if course.how_to_hold == "حضوری":
                    if course.capacity >= 1:
                        course.user.add(student)
                        course.capacity -=1
                        order=Checkout.objects.create(user=student,course=course,is_paid=True,price=course.price,total_price=course.price)
                        course.save()

                        if TeachersIncome.objects.filter(Q(teacher__user=order.course.teacher.user), Q(course=order.course),
                                                            Q(status=False)).exists():

                            teacher_income = TeachersIncome.objects.get(Q(teacher__user=order.course.teacher.user),
                                                                        Q(course=order.course), Q(status=False))
                            teacher_income.income += order.price
                            teacher_income.save()

                        elif TeachersIncome.objects.filter(Q(teacher__user=order.course.teacher.user), Q(course=order.course),
                                                        Q(status=True)).exists():
                            teacher_income = TeachersIncome.objects.create(teacher=order.course.teacher,
                                                                        course=order.course)
                            teacher_income.income += order.price
                            teacher_income.save()

                        else:
                            teacher_income = TeachersIncome.objects.create(teacher=order.course.teacher,
                                                                       course=order.course)
                            teacher_income.income += order.price
                            teacher_income.save()

                    else:

                        context["errors"].append("ظرفیت دوره به اتمام رسیده است")
                        return render(request, "AdminPanel_App/register_student.html", context=context)

                else:
                    course.user.add(student)
                    context["errors"].append("دانشجو به دوره اضافه شد")
                    return render(request, "AdminPanel_App/register_student.html", context=context)

            else:
                context["errors"].append("یوزر انتخاب شده دانشجوی دوره است")
                return render(request, "AdminPanel_App/register_student.html", context=context)

        else:
            context["errors"].append("دانشجویی با این مشخصات وجود ندارد")


            return render(request, "AdminPanel_App/register_student.html", context=context)

        return render(request, "AdminPanel_App/register_student.html", context=context)


    def get(self, request):
        context = {}
        courses = Courses.objects.all()
        context["course"] = courses

        return render(request, "AdminPanel_App/register_student.html", context=context)


class MyDocumentsView(CheckLoginMixin, ListView):
    model = CertificatesOfCourses
    template_name = "AdminPanel_App/my_doucument.html"

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()

        if user.is_admin:

            return qs

        else:

            return qs.filter(user=user)



class BlogListView(CheckBloggerMixin, ListView):
    model = BlogModel
    template_name = "AdminPanel_App/blog_list.html"
    paginate_by = 20

    def get_queryset(self):

        user = self.request.user
        qs = super(BlogListView, self).get_queryset()

        if user.is_admin == True:

            return qs

        else:

            return qs.filter(user=user)


class CreateBlogView(CheckBloggerMixin, View):

    def post(self, request):
        form = CreateBlogForm(request.POST, request.FILES)

        if form.is_valid():
            user = request.user
            b = form.save(commit=False)
            b.user = user
            b.save()

            return redirect(reverse("AdminPanel:blog_list"))

        return render(request, "AdminPanel_App/create_blog.html", {"form": form})

    def get(self, request):
        form = CreateBlogForm()

        return render(request, "AdminPanel_App/create_blog.html", {"form": form})


class UpdateBlogView(AdminEmployeMixin, UpdateView):
    model = BlogModel
    template_name = "AdminPanel_App/update_blog_form.html"
    form_class = UpdateBlogForm
    success_url = reverse_lazy("AdminPanel:blog_list")


class DeleteCourseView(AdminEmployeMixin, DeleteView):
    model = Courses
    success_url = reverse_lazy("AdminPanel:Course_list")


class DeleteCourseChild(CheckIsTeacherMixin, DeleteView):
    model = CoursesChild


    def get_success_url(self):

        video_child=CoursesChild.objects.get(id=self.object.pk)


        return reverse("AdminPanel:video_child_list",kwargs={"pk":video_child.parent.id})


class DeleteCategory(AdminEmployeMixin, DeleteView):
    model = Category

    success_url = reverse_lazy("AdminPanel:Category_course")


class DeleteTeacherView(CheckAdmin, DeleteView):
    model = Teacher
    success_url = reverse_lazy("AdminPanel:Teacher_list")


class MyCourseView(CheckLoginMixin, ListView):
    model = Courses
    template_name = "AdminPanel_App/MyCourse.html"

    def get_queryset(self):
        qs = super(MyCourseView, self).get_queryset()

        return qs.filter(user=self.request.user)


class CreateMessageView(CheckAdmin, View):

    def post(self, request):
        form = CreateMessageForm(request.POST, request.FILES)

        return render(request, "AdminPanel_App/create_message.html", {"form": form})

    def get(self, request):
        form = CreateMessageForm()

        return render(request, "AdminPanel_App/create_message.html", {"form": form})


class Accses(CheckAdmin, View):

    def get(self, request):

        return render(request, "AdminPanel_App/accses.html")

    def post(self, request):
        context = {"errors": []}

        student_number = request.POST.get("user")

        if student_number:

            if User.objects.filter(Q(student_number=student_number) | Q(nation_code=student_number) | Q(
                    phone=student_number)).exists():

                return redirect(reverse("AdminPanel:add_accses_to_user") + f"?student_number={student_number}")
            else:
                context["errors"].append("دانشجویی با این مشخصات وجود ندارد")
                return render(request, "AdminPanel_App/accses.html", context)

        return render(request, "AdminPanel_App/accses.html")


class AddAcsesToUser(CheckAdmin, View):

    def get(self, request):
        student_number = request.GET.get("student_number")
        user_id = User.objects.get(
            Q(student_number=student_number) | Q(nation_code=student_number) | Q(phone=student_number))
        form = AddAcsess(instance=user_id)

        return render(request, "AdminPanel_App/add_acses_to_user.html", {"form": form})

    def post(self, request):
        student_number = request.GET.get("student_number")
        user_id = User.objects.get(
            Q(nation_code=student_number) | Q(student_number=student_number) | Q(phone=student_number))
        form = AddAcsess(request.POST, request.FILES, instance=user_id)

        if form.is_valid():
            form.save()

            return redirect("AdminPanel:add_accses")

        return render(request, "AdminPanel_App/add_acses_to_user.html", {"form": form})


class IncomeTeachersView(CheckTeacherMixin, ListView):
    template_name = "AdminPanel_App/teachersincome.html"
    model = TeachersIncome
    paginate_by = 10

    def get_queryset(self):
        qs = super(IncomeTeachersView, self).get_queryset()

        if self.request.user.is_admin or self.request.user.is_employee:

            return qs

        elif self.request.user.is_teacher:

            return qs.filter(teacher__user=self.request.user)


class ListOfPaymentsView(CheckLoginMixin, ListView):
    template_name = "AdminPanel_App/list_of_pay.html"
    model = Checkout
    paginate_by = 10

    def get_queryset(self):

        qs = super(ListOfPaymentsView, self).get_queryset()

        if self.request.user.is_admin:

            return qs
        else:

            return qs.filter(user=self.request.user)


class EditAdminView(CheckAdmin, View):

    def get(self, request, StudentNumber):
        student_number = StudentNumber

        return redirect(reverse("AdminPanel:add_accses_to_user") + f"?student_number={student_number}")


class EditTeacherIncomeView(AdminEmployeMixin, View):

    def get(self, request, pk):
        income_teacher = TeachersIncome.objects.get(id=pk)
        form = TeacherIncomeForms(instance=income_teacher)

        return render(request, "AdminPanel_App/pay_to_teacher.html", {"form": form})

    def post(self, request, pk):
        income_teacher = TeachersIncome.objects.get(id=pk)
        form = TeacherIncomeForms(data=request.POST, instance=income_teacher)

        if form.is_valid():
            form.save()

            return redirect("AdminPanel:teacher_income")

        return render(request, "AdminPanel_App/pay_to_teacher.html", {"form": form})
