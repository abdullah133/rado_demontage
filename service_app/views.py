from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Services

class ServiceView(TemplateView):
    template_name = 'service_app/service.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['auf_welcher_seite'] = 'service'
        context['home_service'] = Services.objects.all()
        return context
