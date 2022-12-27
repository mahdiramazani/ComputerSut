from django.urls import path
from apps.AdminPanel_App import views

app_name="AdminPanel"
urlpatterns=[
    path("",views.AdminPanelView.as_view(),name="Userpanel"),
    path("admin",views.DashboardView.as_view(),name="Dashboard"),
    path("course_list",views.CourseList.as_view(),name="Course_list"),
    path("students_of_the_course/<int:pk>",views.Students_Of_The_Course.as_view(),name="students_of_the_course"),
    path("add_course",views.AddCourse.as_view(),name="Add_course"),
    path("edit_course/<int:pk>",views.EditCourse.as_view(),name="EditCourse"),
    path("add_video_child/<int:pk>",views.AddVideoChild.as_view(),name="Add_Video_Child"),
    path("video_child_list/<int:pk>",views.VideoChildList.as_view(),name="video_child_list"),
    path("edit_video_child/<int:pk>",views.EditVideoChild.as_view(),name="Edit_Video_Child"),
    path("course_category",views.CategoryCourse.as_view(),name="Category_course"),
    path("create_category",views.CreateCategoryView.as_view(),name="Create_Category"),
    path("edit_category/<int:pk>",views.EditCategory.as_view(),name="Edit_Category"),
    path("coupons",views.Coupons.as_view(),name="Coupons"),
    path("certificates",views.CertificatesOfCoursesView.as_view(),name="CertificatesOfCourses"),
    path("register_student",views.RegisterStudent.as_view(),name="Register_student"),
    path("request_to_teacher",views.RequestToTeacherView.as_view(),name="Request_Teacher"),
    path("edit_teacher/<int:pk>",views.EditTeacherView.as_view(),name="edit_teacher"),
    path("admin_list",views.AdminList.as_view(),name="Admin_list"),
    path("add_admin",views.AddAdmin.as_view(),name="Add_admin"),
    path("add_teacher",views.AddTeacher.as_view(),name="Add_teacher"),
    path("teacher_list",views.TeacherList.as_view(),name="Teacher_list"),
    path("student_list",views.StudentList.as_view(),name="Student_list"),
    path("add_student",views.AddStudent.as_view(),name="Add_student"),
    path("my_documents",views.MyDocumentsView.as_view(),name="MyDocuments"),
    path("requests",views.RequestsView.as_view(),name="requests"),
    path("request_list",views.RequestListView.as_view(),name="request_list"),
    path("request_list_update/<int:pk>",views.RequestListUpdate.as_view(),name="request_list_update"),
    path("blog_list",views.BlogListView.as_view(),name="blog_list"),
    path("create_blog",views.CreateBlogView.as_view(),name="create_blog"),
    path("update_blog/<int:pk>",views.UpdateBlogView.as_view(),name="update_blog"),
    path("delete_course/<int:pk>",views.DeleteCourseView.as_view(),name="delete_course"),
    path("delet_video_child/<int:pk>",views.DeleteCourseChild.as_view(),name="delete_video_child"),
    path("delete_category/<int:pk>",views.DeleteCategory.as_view(),name="delete_category"),
    path("delete_teacher/<int:pk>",views.DeleteTeacherView.as_view(),name="delete_teacher"),
    path("my_course",views.MyCourseView.as_view(),name="my_course"),
]