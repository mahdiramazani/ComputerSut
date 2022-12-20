from django.urls import path
from . import views

app_name="Course_app"
urlpatterns=[

    path("",views.CoursesView.as_view(),name="Course"),
    path("course_detail/<int:pk>",views.CourseDetailView.as_view(),name="Course_detail"),
    path("course_detail/video_detail/<int:pk>",views.CourseDetailVideoView.as_view(),name="video_detail")
]