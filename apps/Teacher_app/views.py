from django.shortcuts import render,redirect
from django.views.generic import View,ListView,TemplateView
from apps.Acount_app.models import User,Teacher
from apps.Course_app.models import Courses
class TeacherListView(ListView):

    template_name = "Teacher_app/teachers_list.html"
    model=Teacher
    paginate_by = 10

    def get_queryset(self):

        q=super().get_queryset()


        return q.filter(status = True)


    def get_context_data(self, *, object_list=None, **kwargs):

        context=super(TeacherListView, self).get_context_data(**kwargs)

        context["best_teacher"]=Teacher.objects.all()

        return context


class TeacherDetail(View):

    def get(self,request,id):


        teacher=Teacher.objects.get(id=id)

        course=Courses.objects.filter(teacher=teacher)


        return render(request,"Teacher_app/eacher_detail.html",{"teacher":teacher,"course":course})


