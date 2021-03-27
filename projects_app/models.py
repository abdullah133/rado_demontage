from django.db import models
from django.urls import reverse
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
from django.utils.html import format_html
from django.conf import settings
from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageRatioField
from easy_thumbnails.signals import thumbnail_created

class Kategorien(models.Model):
    kategorie_name = models.CharField(max_length=30,blank=True, null=True,)

    def __str__(self):
        return "%s" % (self.kategorie_name)

    class Meta:
        verbose_name_plural = " Kategorien"
        verbose_name = "Kategorie"

    def get_absolute_url(self):
        return reverse('base_app:home_page')


class Projects(models.Model):
    kategorie = models.ForeignKey(Kategorien, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=40, blank=False, null=False,)
    bild = models.ImageField('Bild',blank=True, upload_to='projects/%m/')
    description = models.TextField(blank=True, null=True)
    cropping = ImageRatioField('bild', '800x600')

    class Meta:
        verbose_name_plural = "Projekte"
        verbose_name = "Projekt"


    def __str__(self):
        return self.title

    def get_cropping_as_list(self):
        if self.cropping:
            return list(map(int, self.cropping.split(',')))

    def image_tag_admin(self):
        if self.bild:
            return format_html('<img src="{}" width="150" height="150" />'.format(self.bild.url))
        else:
            return 'Hier ist noch kein Bild vorhanden'
    image_tag_admin.short_description = 'Bild'

    def image_tag_png(self):
        if self.bild:
            thumbnail_url = get_thumbnailer(self.bild).get_thumbnail({
                'size': (800, 600),
                'box': self.cropping,
                'crop': True,
                'detail': True,
                }).url
        return format_html('<img src="{}" class="img-responsive" alt="{}_Webdesinger in Wien" />'.format(thumbnail_url,self.title))

    def get_detail_url(self):
        return reverse('projects_app:projects_detail_page', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('base_app:home_page')
