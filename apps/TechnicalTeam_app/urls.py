from django.urls import path
from apps.TechnicalTeam_app import views

app_name="TechnicalTeam_app"
urlpatterns=[

    path("",views.TechnicalTeamView.as_view(),name="technical_team")
]