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
    facebook_link = models.CharField('Facebook Link',max_length=300, blank=True, null=True)
    instagram_link = models.CharField('Instagram Link',max_length=300, blank=True, null=True)
    unternehmens_sitz = models.CharField(max_length=355, default='Sitz: Hirm')
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Kontaktdaten"
        verbose_name = "Kontaktdaten"

    def unternehmens_name(self):
        current_site = self.website.get_current()
        return current_site.name


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

    def get_absolute_url(self):
        return reverse('base_app:home_page')
