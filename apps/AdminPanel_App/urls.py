from django.urls import path
from apps.AdminPanel_App import views

app_name="AdminPanel"
urlpatterns=[
    path("",views.AdminPanelView.as_view(),name="Userpanel"),
    path("admin",views.DashboardView.as_view(),name="Dashboard"),
    path("course_list",views.CourseList.as_view(),name="Course_list"),
    path("add_course",views.AddCourse.as_view(),name="Add_course"),
    path("edit_course/<int:pk>",views.EditCourse.as_view(),name="EditCourse"),
    path("add_video_child/<int:pk>",views.AddVideoChild.as_view(),name="Add_Video_Child"),
    path("video_child_list/<int:pk>",views.VideoChildList.as_view(),name="video_child_list"),
    path("edit_video_child/<int:pk>",views.EditVideoChild.as_view(),name="Edit_Video_Child"),
    path("course_category",views.CategoryCourse.as_view(),name="Category_course"),
    path("create_category",views.CreateCategoryView.as_view(),name="Create_Category"),
    path("edit_category/<int:pk>",views.EditCategory.as_view(),name="Edit_Category"),
    path("coupons",views.Coupons.as_view(),name="Coupons"),
    path("register_student",views.RegisterStudent.as_view(),name="Register_student"),
    path("request_to_teacher",views.RequestToTeacherView.as_view(),name="Request_Teacher"),
    path("admin_list",views.AdminList.as_view(),name="Admin_list"),
    path("add_admin",views.AddAdmin.as_view(),name="Add_admin"),
    path("add_teacher",views.AddTeacher.as_view(),name="Add_teacher"),
    path("teacher_list",views.TeacherList.as_view(),name="Teacher_list"),
    path("student_list",views.StudentList.as_view(),name="Student_list"),
    path("add_student",views.AddStudent.as_view(),name="Add_student")
]