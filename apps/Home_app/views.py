from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, View
from apps.Acount_app.models import User, Teacher
from apps.Course_app.models import Courses, CoursesChild, Category
from apps.Blog_App.models import BlogModel
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class HomeView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coures = Courses.objects.all()
        teacher = Teacher.objects.filter(status=True)
        category = Category.objects.all()
        last_blog = BlogModel.objects.all()[:3]

        context["coures"] = coures
        context["teacher"] = teacher
        context["category"] = category
        context["object_list"] = last_blog

        return context

    template_name = "Home_app/home.html"


class FaqQuestionView(TemplateView):
    template_name = "Home_app/faq.html"


class SearchView(View):

    def get(self, request):
        name = request.GET.get("q")
        page = request.GET.get('page', 1)

        if Courses.objects.filter(
            Q(titel__icontains=name) | Q(teacher__user__full_name__icontains=name) | Q(
                Introduction_of_the_valley__icontains=name) | Q(category__name__icontains=name)).exists():
            paginator = Paginator(object, 6)

            try:
                object_list= paginator.page(page)

            except PageNotAnInteger:
                object_list = paginator.page(1)
            except EmptyPage:
                object_list = paginator.page(paginator.num_pages)

            return render(request, "Home_app/search.html", {"object_list": object_list})

        else:
            return render(request, "Home_app/search.html", {"object_list": None,"errors":f"نتیجه ای برای {name} یافت نشد"})