from django.urls import path
from . import views


app_name="Acount_app"
urlpatterns=[

        path("signup",views.SignUpView.as_view(),name="Signup"),
        path("login",views.LoginView.as_view(),name="Login"),
        path("logout",views.LogOut.as_view(),name="Logout")
]