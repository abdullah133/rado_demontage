from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import ImpressumModel


class ImpressumView(TemplateView):
    template_name = 'impressum_app/impressum.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['impressum'] = ImpressumModel.objects.all()
        return context
