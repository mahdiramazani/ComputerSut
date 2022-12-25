from django.shortcuts import render
from django.views.generic import View,TemplateView



class ContactView(TemplateView):
    template_name = "CountactByMe_app/contact.html"
