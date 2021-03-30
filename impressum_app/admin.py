from django.contrib import admin
from .models import ImpressumModel


@admin.register(ImpressumModel)
class ImpressumModelAdmin(admin.ModelAdmin):
    list_display = ['title','ordering','description', ]
    list_editable  = ['ordering',]
    ordering = ('ordering',)
