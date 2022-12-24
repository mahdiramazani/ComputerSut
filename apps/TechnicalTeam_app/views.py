from django.shortcuts import render
from apps.Acount_app.models import User
from django.views.generic import View,TemplateView,ListView



class TechnicalTeamView(ListView):
    model = User
    template_name = "TechnicalTeam_app/technical_team.html"

    def get_queryset(self):

        qs=super().get_queryset()

        return qs.filter(is_technical_team = True)

