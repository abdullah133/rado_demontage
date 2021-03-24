from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Projects


from django.views.generic.detail import DetailView


class ProjectDetailView(DetailView):
    model = Projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
