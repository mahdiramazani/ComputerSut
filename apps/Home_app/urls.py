from django.urls import path
from . import views

app_name="Home_app"
urlpatterns=[
    path("", views.HomeView.as_view(), name="Home"),
    path("faq/",views.FaqQuestionView.as_view(),name="faq")
]