from django.urls import path
from . import views


app_name="CountactByMe_app"
urlpatterns=[

    path("",views.ContactView.as_view(),name="contact")
]