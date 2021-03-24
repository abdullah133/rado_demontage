from django.contrib import admin
from .models import AboutDescription, AboutImg, TeamModel
from django.contrib.sites.models import Site
from django import forms
from image_cropping import ImageCropWidget
from django.template.response import TemplateResponse
from image_cropping import ImageCroppingMixin

class ProjectsForm(forms.ModelForm):
    class Media:
        widgets = {
            'bild': ImageCropWidget,
        }


@admin.register(TeamModel)
class TeamModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name','position','image_tag_admin']

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': False,
            'show_save_and_continue': True,
            'show_delete': True,
            'show_save_and_add_another':False,
        })
        return super().render_change_form(request, context, add, change, form_url, obj)


@admin.register(AboutDescription)
class AboutDescriptionAdmin(admin.ModelAdmin):
    list_display = ['title','description']


@admin.register(AboutImg)
class AboutImgAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag_webp']
    exclude = ['bild_png','bild_webp']
