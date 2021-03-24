from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import AboutDescription, AboutImg, TeamModel


class AboutView(TemplateView):
    template_name = 'about_app/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_descriptions'] = AboutDescription.objects.all()

        context['about_text'] = AboutImg.objects.first()
        context['team_model'] = TeamModel.objects.all()
        context['auf_welcher_seite'] = 'about'
        return context
