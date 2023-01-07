from django.shortcuts import render
from django.views.generic import TemplateView
from apps.Acount_app.models import User,Teacher
from apps.Course_app.models import Courses,CoursesChild,Category


class HomeView(TemplateView):


    def get_context_data(self, **kwargs):

        context=super().get_context_data(**kwargs)
        coures=Courses.objects.all()
        teacher=Teacher.objects.filter(status=True)
        category=Category.objects.all()

        context["coures"]=coures
        context["teacher"]=teacher
        context["category"]=category

        return context

    template_name = "Home_app/home.html"


class FaqQuestionView(TemplateView):

    template_name = "Home_app/faq.html"