from django.urls import path
from apps.Teacher_app import views

app_name="Teacher_app"
urlpatterns=[

    path("",views.TeacherListView.as_view(),name="Teacher_List"),
    path("detail/<int:id>/",views.TeacherDetail.as_view(),name="Teacher_Detail"),


]
