from django.shortcuts import render,redirect
from django.views.generic.base import View
from apps.Acount_app.forms import SignForm,LoginForm
from apps.Acount_app.models import User
from django.contrib.auth import login,logout,authenticate
from django.db.models import Q


class SignUpView(View):



    def post(self,request):

        form=SignForm(data=request.POST)

        if form.is_valid():
            cd=form.cleaned_data
            phone =cd.get("phone")
            full_name =cd.get("full_name")
            student_number =cd.get("student_number")
            password1 =cd.get("password1")
            password2 =cd.get("password2")
            university_name = cd.get("university_name")
            major = cd.get("major")

            user=User.objects.create(phone=phone,full_name=full_name,student_number=student_number,password=password1,university_name=university_name,major=major)

            user.set_password(password1)
            user.save()

            login(request,user)
            return redirect("Home_app:Home")



        return render(request,"Acount_app/signup.html",{"form":form})

    def get(self,request):
        form=SignForm()


        return render(request,"Acount_app/signup.html",{"form":form})


class LoginView(View):

    def post(self,request):
        form=LoginForm(data=request.POST)

        if form.is_valid():

            cd=form.cleaned_data
            phone=cd.get("phone")
            password=cd.get("password")

            user=authenticate(username=phone,password=password)

            if user is not None:

                login(request,user,backend="allauth.account.auth_backends.AuthenticationBackend")

                return redirect("Home_app:Home")

            else:

                form.add_error("phone","نام کاربری یا رمز عبور اشتباه است")

        return render(request,"Acount_app/login.html",{"form":form})


    def get(self,request):
        form=LoginForm()


        return render(request,"Acount_app/login.html",{"form":form})



class LogOut(View):

    def get(self,request):


        logout(request)


        return redirect("Home_app:Home")


