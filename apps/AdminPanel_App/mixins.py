from apps.Acount_app.models import User,Teacher
from django.shortcuts import redirect

class CheckTeacherMixin:

    def dispatch(self,request,*args,**kwargs):

        user=request.user

        if (user.is_teacher == True) or (user.is_admin == True):


            return super().dispatch(request,*args,**kwargs)

        else:



            return redirect("Home_app:Home")
