from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from .models import BlogModel


class BlogHomeView(ListView):

    template_name = "Blog_App/blog.html"
    model = BlogModel

    







