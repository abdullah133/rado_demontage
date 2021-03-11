from django.db import models
from django.urls import reverse

class AboutContent(models.Model):
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "About me Contents "
        verbose_name = "About me Content"

    def get_absolute_url(self):
        return reverse('about_app:about_page')
