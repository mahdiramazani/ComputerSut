from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from .forms import CountactUsForm

class ContactView(View):


    def post(self,request):
        form=CountactUsForm(data=request.POST)


        if form.is_valid():

            form.save()


            return redirect("CountactByMe_app:contact")


        return render(request,"CountactByMe_app/contact.html",{"form":form})

    def get(self,request):
        form=CountactUsForm()


        return render(request,"CountactByMe_app/contact.html",{"form":form})


