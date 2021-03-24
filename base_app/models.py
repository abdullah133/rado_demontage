from django.db import models
from django.utils.html import format_html
from info_app.models import KontaktDatenModel
from django.contrib.sites.models import Site
from django.urls import reverse
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
from django.conf import settings
import datetime

class MasterObjekt(object):

    def __init__(self, request):
        super(MasterObjekt, self).__init__()
    def homepage_obj(self):
        current_site = Site.objects.first()
        return current_site

    def homepage_name(self):
        return self.homepage_obj().name

    def homepage_url(self):
        name = self.homepage_obj().domain
        return 'https://{}/'.format(name)

    def kontakt_daten_obj(self):
        current_site = KontaktDatenModel.objects.first()
        return current_site

    def feature_tag(self, titel_1, titel_2):
        return format_html('<li><h4 class="tv-checkmark"><span>{}</span></h4><div class="tv-feature-text">{}</div></li>'.format(titel_1,titel_2))

    def feature_tag_1(self):
        titel_1 = self.kontakt_daten_obj().telefon
        titel_2 = self.kontakt_daten_obj().adresse
        print('kontakt dateb :'+str(titel_2))
        return self.feature_tag(titel_1,titel_2)

    def feature_tag_2(self):
        titel_1 = self.kontakt_daten_obj().email
        titel_2 = self.kontakt_daten_obj().ort
        return self.feature_tag(titel_1,titel_2)

    def feature_tag_3(self):
        titel_1 = 'Zertifiziert'
        titel_2 = self.kontakt_daten_obj().ust_idnr
        return self.feature_tag(titel_1,titel_2)

    def time_year(self):
        heute = datetime.datetime.now()
        return heute.year

    def abdullah_webdesign_image_tag(self):
        png_image_url = settings.STATIC_URL + 'base_app/img/my_icon.webp'
        webp_image_url = settings.STATIC_URL + 'base_app/img/my_icon.webp'
        alt_text = 'webdesigner in wien'
        return format_html('<img src="{}" height="25" width="25" onerror="{}{}{}" alt="{}" />'.format(webp_image_url,"this.src='",png_image_url,"'",alt_text))

    def abdullah_webdesign_tag(self):

        image_tag = self.abdullah_webdesign_image_tag()
        return format_html('<a href="https://www.kroums-webdesign.at" target="_blank" rel="nofollow noopener"> {} by Kroums-Webdesign</a>'.format(image_tag))


class HomeSlider(models.Model):
    title = models.CharField('Titel',max_length=300)
    title_description = models.TextField('Untertitel',blank=True, null=True)
    description = models.TextField('Beschreibung',blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Beschreibungen und Bilder "
        verbose_name = "Beschreibung und Bild"

    def get_absolute_url(self):
        return reverse('base_app:home_page')
