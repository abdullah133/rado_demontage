from django.db import models

# Create your models here.

class ImpressumModel(models.Model):
    ordering = models.IntegerField("Reihenfolge", default=1)
    title = models.CharField('Titel',max_length=300)
    description = models.TextField('Beschreibung',blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Impressum und AGB's "
        verbose_name = "Impressum oder AGB"
        ordering = ('ordering',)

    def get_absolute_url(self):
        return reverse('impressum_app:impressum_page')
