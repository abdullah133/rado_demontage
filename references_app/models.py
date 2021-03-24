from django.db import models
from smartfields.processors import ImageProcessor
from image_cropping import ImageRatioField
from easy_thumbnails.files import get_thumbnailer
from django.utils.html import format_html
from django.urls import reverse

class ReferencesModel(models.Model):
    title = models.CharField('Titel',max_length=300)
    description = models.TextField('text', blank=True, null=True)
    bild = models.ImageField('Bild',blank=True, upload_to='references/%m/')
    cropping = ImageRatioField('bild', '777x500')


    class Meta:
        verbose_name_plural = "Referenzen"
        verbose_name = "Referenz"


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
                'size': (777, 500),
                'box': self.cropping,
                'crop': True,
                'detail': True,
                }).url
        return format_html('<img src="{}" alt="{}_Rado-Montage" class="img-responsive" />'.format(thumbnail_url,self.title))

    def get_absolute_url(self):
        return reverse('references_app:references_page')


class ReferencesText(models.Model):
    title = models.CharField('Titel',max_length=300)
    description = models.TextField('text', blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Beschreibungen unserer Referenzen"
        verbose_name = "Beschreibung unserer Referenzen"

    def get_absolute_url(self):
        return reverse('references_app:references_page')
