from django.contrib import admin
from .models import Kategorien, Projects
from django.contrib.sites.models import Site
from django import forms
from image_cropping import ImageCropWidget
from django.template.response import TemplateResponse
from image_cropping import ImageCroppingMixin

def save_ob(modeladmin, request, queryset):

    for element in queryset:
        element.save()

save_ob.short_description = "copy_bauteil_to_new_path"




class ProjectsForm(forms.ModelForm):
    class Media:
        widgets = {
            'bild': ImageCropWidget,
        }


@admin.register(Projects)
class ProjectsAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['title','description','kategorie','image_tag_admin']
    actions = [save_ob]

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': False,
            'show_save_and_continue': True,
            'show_delete': True,
            'show_save_and_add_another':False,
        })
        return super().render_change_form(request, context, add, change, form_url, obj)



@admin.register(Kategorien)
class KategorienAdmin(admin.ModelAdmin):
    list_display = ['kategorie_name']
