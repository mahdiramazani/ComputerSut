from django.shortcuts import redirect
class CheckLogin:


    def dispatch(self,request):


        if request.user.is_authenticated:

            return redirect("Home_app:Home")

        else:

            return super().dispatch(request)