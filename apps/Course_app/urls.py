from django.urls import path
from . import views

app_name="Course_app"
urlpatterns=[

    path("",views.CoursesView.as_view(),name="Course"),
    path("course_detail/<int:pk>",views.CourseDetailView.as_view(),name="Course_detail"),
    path("course_detail/video_detail/<int:pk>",views.CourseDetailVideoView.as_view(),name="video_detail"),
    path("category/<int:id>/",views.CategoryCourse.as_view(),name="Category_course"),
    path("AddCourseToOrder/<int:pk>/",views.AddCourseToOrderView.as_view(),name="AddCourseToOrder"),
    path("checkout/",views.CheckOutClass.as_view(),name="checkout"),
    path("requestPay/<int:pk>/",views.RequestPay.as_view(),name="request_pay"),
    path("verify/",views.VerifyView.as_view(),name="verify"),
    path("document_inquiry/",views.DocumentInquiryView.as_view(),name="document_inquiry"),
    path("document/",views.DocumentView.as_view(),name="document")
]