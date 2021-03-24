from django.contrib import admin
from .models import ReferencesModel, ReferencesText
from image_cropping import ImageCropWidget
from image_cropping import ImageCroppingMixin
from django.contrib.sites.models import Site
from django import forms

class ProjectsForm(forms.ModelForm):
    class Media:
        widgets = {
            'bild': ImageCropWidget,
        }


@admin.register(ReferencesModel)
class ReferencesModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['title','description','image_tag_admin']

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': False,
            'show_save_and_continue': True,
            'show_delete': True,
            'show_save_and_add_another':False,
        })
        return super().render_change_form(request, context, add, change, form_url, obj)


@admin.register(ReferencesText)
class ReferencesTextAdmin(admin.ModelAdmin):
    list_display = ['title','description']
