from django.db import models

from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
from django.urls import reverse
from django.utils.html import format_html
from django.conf import settings
from django.contrib.sites.models import Site

class KontaktDatenModel(models.Model):
    name = models.CharField(max_length=355, default='AMBags')
    website = models.OneToOneField(Site, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=300, default='info@ambags.ch')
    adresse = models.CharField(max_length=355, default='Ringstrasse 12A')
    ort = models.CharField(max_length=355, default='9200 Gossau')
    telefon = models.CharField('Telefon Nr.',max_length=300, blank=True, null=True)
    ust_idnr = models.CharField('UST-IDNr',max_length=300, blank=True, null=True)
    logo = fields.ImageField("Logo",upload_to='logo/', blank=True,dependencies=[FileDependency(attname='logo_webp', processor=ImageProcessor(format='WEBP', scale={'max_height': 350})),FileDependency(attname='logo_png', processor=ImageProcessor(format='PNG', scale={'max_height': 350}))])
    logo_webp = fields.ImageField("Logo .webp",upload_to='', blank=True)
    logo_png = fields.ImageField("Logo .png",upload_to='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Kontaktdaten"
        verbose_name = "Kontaktdaten"

    def logo_tag(self):
        return format_html('<img alt="{}" class="img-fluid" src="{}" onerror="{}{}{}" />'.format(self.name,self.logo_webp.url,"this.src='",self.logo_png.url,"'"))

    def image_tag_admin(self):
        if self.logo_png:
            return format_html('<img src="{}" width="300" height="150" />'.format(self.logo_png.url))
        else:
            return 'Hier ist noch kein Bild vorhanden'

    image_tag_admin.short_description = 'Logo'

    def homepage_name(self):
        current_site = self.website.get_current()
        return current_site.name
    def homepage_domain(self):
        current_site = self.website.get_current()
        return current_site.domain

    def homepage_url(self):
        name = self.homepage_domain()
        return 'https://www.{}/'.format(name)

    def get_home_url(self):
        return reverse('base_app:home_page')
