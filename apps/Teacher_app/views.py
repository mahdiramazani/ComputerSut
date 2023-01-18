from django.shortcuts import render,redirect
from django.views.generic import View,ListView,TemplateView
from apps.Acount_app.models import User,Teacher

class TeacherListView(ListView):

    template_name = "Teacher_app/teachers_list.html"
    model=Teacher
    paginate_by = 1

    def get_queryset(self):

        q=super().get_queryset()


        return q.filter(status = True)


    def get_context_data(self, *, object_list=None, **kwargs):

        context=super(TeacherListView, self).get_context_data(**kwargs)

        context["best_teacher"]=Teacher.objects.all()

        return context



