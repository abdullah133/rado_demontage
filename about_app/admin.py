from django.contrib import admin
from .models import AboutContent

# Register your models here.
@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ['description']
