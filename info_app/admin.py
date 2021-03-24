from django.contrib import admin
from .models import KontaktDatenModel
from django import forms



@admin.register(KontaktDatenModel)
class KontaktDatenModelAdmin(admin.ModelAdmin):
    list_display = ['name','email','adresse','telefon']
