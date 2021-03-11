from django.contrib import admin
from .models import KontaktDatenModel
from django import forms



@admin.register(KontaktDatenModel)
class KontaktDatenModelAdmin(admin.ModelAdmin):
    list_display = ['name','email','image_tag_admin']
    exclude = ['logo_webp','logo_png']
