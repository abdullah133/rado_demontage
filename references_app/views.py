from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import ReferencesModel, ReferencesText


class ReferencesView(TemplateView):
    template_name = 'references_app/references.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['references'] = ReferencesModel.objects.all()
        context['references_description'] = ReferencesText.objects.all()
        context['auf_welcher_seite'] = 'references'
        return context
