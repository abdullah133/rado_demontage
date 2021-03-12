from django.contrib import admin
from .models import HomeSlider, HomeDescription, HomeText, HomeBand, HomeImg, HomeService

@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['title','title_description','description']

@admin.register(HomeDescription)
class HomeDescriptionAdmin(admin.ModelAdmin):
    list_display = ['title','description']

@admin.register(HomeText)
class HomeTextAdmin(admin.ModelAdmin):
    list_display = ['title','description']

@admin.register(HomeBand)
class HomeBandAdmin(admin.ModelAdmin):
    list_display = ['title','description','image_tag_webp']
    exclude = ['bild_png','bild_webp']

@admin.register(HomeImg)
class HomeImgAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag_webp']
    exclude = ['bild_png','bild_webp']

@admin.register(HomeService)
class HomeServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
