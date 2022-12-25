from django.urls import path
from . import views

urlpatterns=[

    path("",views.BlogHomeView.as_view(),name="blog")

]