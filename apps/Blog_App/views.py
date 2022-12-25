from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from .models import BlogModel
from apps.Course_app.models import Category

class BlogHomeView(ListView):

    template_name = "Blog_App/blog.html"
    model = BlogModel



class DetailBlogView(DetailView):

    model = BlogModel
    template_name = "Blog_App/blog-detail.html"

    def get_context_data(self, **kwargs):

        context=super().get_context_data(**kwargs)
        category=Category.objects.all()
        context["category"]=category

        blog=BlogModel.objects.get(id=self.object.id)
        blog.view += 1
        blog.save()

        return context










