from django.urls import path
from . import views


app_name="Blog_App"
urlpatterns=[

    path("",views.BlogHomeView.as_view(),name="blog"),
    path("detail/<int:pk>",views.DetailBlogView.as_view(),name="blog_detail")

]