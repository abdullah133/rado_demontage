from django.db import models
from django.urls import reverse

# Create your models here.

class ContactInfo(models.Model):
    name = models.CharField('Name',max_length=300, default="Abdullah Kroum")
    telefon = models.CharField('Telefon Nr.',max_length=300, blank=True, null=True)
    email = models.CharField('E-Mail',max_length=300)
    adresse = models.CharField('Adresse',max_length=300, default="Abdullah Kroum")
    facebook_link = models.CharField('Facebook Link',max_length=300, blank=True, null=True)


    class Meta:
        verbose_name_plural = " contact infos"
        verbose_name = "info"

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('base_app:home_page')
