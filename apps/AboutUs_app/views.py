from django.shortcuts import render
from django.views.generic import TemplateView
from apps.Acount_app.models import User


class AboutUsView(TemplateView):

    template_name="AboutUs_app/about.html"
