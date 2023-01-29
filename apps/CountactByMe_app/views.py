from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from .models import ContactUs
from .forms import CountactUsForm
from django.http import JsonResponse
class ContactView(View):


    def post(self,request):
        form = CountactUsForm(request.POST)

        name=request.POST.get("name")
        phone=request.POST.get("phone")
        body=request.POST.get("body")



        if name and body and phone:
            ContactUs.objects.create(full_name=name,phone_number=phone,body=body)
            message=f"{name} عزیز پیام شما ارسال شد"
            return JsonResponse({"response":message})



        return render(request,"CountactByMe_app/contact.html",{"form":form})

    def get(self,request):
        form=CountactUsForm()


        return render(request,"CountactByMe_app/contact.html",{"form":form})


