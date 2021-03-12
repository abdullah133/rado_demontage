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
    title_description = models.TextField('Titels Zusatz',blank=True, null=True)
    description = models.TextField('Beschreibung',blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Die Beschreibungen mit den Bildern auf die Homeseite "
        verbose_name = "Eine Beschreibung mit den Bildern auf die Homeseite"

    def get_absolute_url(self):
        return reverse('base_app:home_page')


class HomeDescription(models.Model):
    title = models.CharField('Titel',max_length=300)
    description = models.TextField('Beschreibung', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Die Beschreibungen auf die Homeseite "
        verbose_name = "Eine Beschreibung auf die Homeseite"

    def get_absolute_url(self):
        return reverse('base_app:home_page')


class HomeText(models.Model):
    title = models.CharField('Titel',max_length=300)
    description = models.TextField('text', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Der erste Text auf Die Homseite"
        verbose_name = "Der erste Text auf Die Homseite"

    def get_absolute_url(self):
        return reverse('base_app:home_page')


class HomeBand(models.Model):
    title = models.CharField('Titel',max_length=300)
    description = models.TextField('text', blank=True, null=True)
    bild = fields.ImageField(upload_to='photo/%m/',blank=True, null=True , dependencies=[FileDependency(attname='bild_png', processor=ImageProcessor(format='PNG', scale={'max_width': 340, 'max_height': 260})),FileDependency(attname='bild_webp', processor=ImageProcessor(format='WEBP', scale={'max_width': 340, 'max_height': 260}))])
    bild_png = fields.ImageField(upload_to='',blank=True, null=True)
    bild_webp = fields.ImageField(upload_to='',blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Die Beschreibungen im Band auf die Homseite"
        verbose_name = "Beschreibung im Band auf die Homseite"



    def png_image_url(self):
        if self.bild_png:
            png_image_url = self.bild_png.url
        else:
            png_image_url = settings.STATIC_URL + 'base_app/img/kein_bild_vorhanden.png'
        return png_image_url

    def webp_image_url(self):
        if self.bild_webp:
            webp_image_url = self.bild_webp.url
        else:
            webp_image_url = settings.STATIC_URL + 'base_app/img/kein_bild_vorhanden.webp'
        return webp_image_url

    def image_gesamt_tag(self):
        png_image_url = self.png_image_url()
        webp_image_url = self.webp_image_url()
        return format_html('<img src="{}" height="341" onerror="{}{}{}" alt="{}" class="img-responsive" />'.format(webp_image_url,"this.src='",png_image_url,"'",self.title))

    image_gesamt_tag.short_description = 'Bild gesamttag'

    def image_tag(self):
        if self.bild_png:
            return format_html('<img src="{}" width="150" height="150" />'.format(self.bild_png.url))
        else:
            return format_html('<img src="{}" width="150" height="150" />'.format(settings.STATIC_URL + 'base_app/img/kein_bild_vorhanden.png'))

    image_tag.short_description = 'Bild'

    def image_tag_webp(self):
        if self.bild_webp:
            return format_html('<img src="{}" width="150" height="150" />'.format(self.bild_webp.url))
        else:
            return format_html('<img src="{}" width="150" height="150" />'.format(settings.STATIC_URL + 'base_app/img/kein_bild_vorhanden.webp'))
    image_tag_webp.short_description = 'Bild in .webp Format'



    def get_absolute_url(self):
        return reverse('base_app:home_page')

class HomeImg(models.Model):
    title = models.CharField('Titel',max_length=300, default="Rado-Montage")
    bild = fields.ImageField(upload_to='photo/%m/',blank=True, null=True , dependencies=[FileDependency(attname='bild_png', processor=ImageProcessor(format='PNG', scale={'max_width': 340, 'max_height': 260})),FileDependency(attname='bild_webp', processor=ImageProcessor(format='WEBP', scale={'max_width': 340, 'max_height': 260}))])
    bild_png = fields.ImageField(upload_to='',blank=True, null=True)
    bild_webp = fields.ImageField(upload_to='',blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Das Foto Auf die Homeseite"
        verbose_name = "Das Foto auf die Homseite"



    def png_image_url(self):
        if self.bild_png:
            png_image_url = self.bild_png.url
        else:
            png_image_url = settings.STATIC_URL + 'base_app/img/kein_bild_vorhanden.png'
        return png_image_url

    def webp_image_url(self):
        if self.bild_webp:
            webp_image_url = self.bild_webp.url
        else:
            webp_image_url = settings.STATIC_URL + 'base_app/img/kein_bild_vorhanden.webp'
        return webp_image_url

    def image_gesamt_tag(self):
        png_image_url = self.png_image_url()
        webp_image_url = self.webp_image_url()
        return format_html('<img src="{}" onerror="{}{}{}" alt="Über Rado-Montage" class="img-responsive" />'.format(webp_image_url,"this.src='",png_image_url,"'"))

    image_gesamt_tag.short_description = 'Bild gesamttag'

    def image_tag(self):
        if self.bild_png:
            return format_html('<img src="{}" width="150" height="150" />'.format(self.bild_png.url))
        else:
            return format_html('<img src="{}" width="150" height="150" />'.format(settings.STATIC_URL + 'base_app/img/kein_bild_vorhanden.png'))

    image_tag.short_description = 'Bild'

    def image_tag_webp(self):
        if self.bild_webp:
            return format_html('<img src="{}" width="150" height="150" />'.format(self.bild_webp.url))
        else:
            return format_html('<img src="{}" width="150" height="150" />'.format(settings.STATIC_URL + 'base_app/img/kein_bild_vorhanden.webp'))
    image_tag_webp.short_description = 'Bild in .webp Format'

    def get_absolute_url(self):
        return reverse('base_app:home_page')


class HomeService(models.Model):
    title = models.CharField('Leistung',max_length=300, default="Rado-Montage")
    description = models.TextField('Beschreibung der Leistung', blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Unsere Leistungen"
        verbose_name = "Leistung"

    def get_absolute_url(self):
        return reverse('base_app:home_page')
