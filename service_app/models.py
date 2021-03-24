from django.db import models
from smartfields import fields
from django.conf import settings
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
from django.utils.html import format_html
from django.urls import reverse

class Services(models.Model):
    title = models.CharField('Leistung',max_length=300, default="Rado-Montage")
    description = models.TextField('Beschreibung der Leistung', blank=True, null=True)
    bild = models.ImageField('Bild ohne Hintergrund',blank=True, upload_to='über_uns_bilder/%m/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Unsere Leistungen"
        verbose_name = "Leistung"

    def image_tag_admin(self):
        if self.bild:
            return format_html('<img src="{}"/>'.format(self.bild.url))
        else:
            return 'Hier ist noch kein Bild vorhanden'
    image_tag_admin.short_description = 'Bild'

    def get_absolute_url(self):
        return reverse('base_app:home_page')
