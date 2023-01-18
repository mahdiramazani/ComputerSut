from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from apps.Acount_app.models import User,Teacher
from apps.Course_app.models import Courses,CoursesChild,Category
from apps.Blog_App.models import BlogModel


class HomeView(TemplateView):


    def get_context_data(self, **kwargs):

        context=super().get_context_data(**kwargs)
        coures=Courses.objects.all()
        teacher=Teacher.objects.filter(status=True)
        category=Category.objects.all()
        last_blog=BlogModel.objects.all()[:3]

        context["coures"]=coures
        context["teacher"]=teacher
        context["category"]=category
        context["object_list"]=last_blog


        return context

    template_name = "Home_app/home.html"


class FaqQuestionView(TemplateView):

    template_name = "Home_app/faq.html"


