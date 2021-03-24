from django.db import models
from django.urls import reverse
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
from django.conf import settings
from django.utils.html import format_html
from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageRatioField
from easy_thumbnails.signals import thumbnail_created



class TeamModel(models.Model):
    name = models.CharField('Name',max_length=300)
    position = models.CharField('Aufgabenbereich',max_length=300)
    photo = models.ImageField('Foto',blank=True, upload_to='team/%m/')
    cropping = ImageRatioField('photo', '400x465')


    class Meta:
        verbose_name_plural = "Teammitglieder"
        verbose_name = "Teammitglied"


    def __str__(self):
        return self.name

    def get_cropping_as_list(self):
        if self.cropping:
            return list(map(int, self.cropping.split(',')))

    def image_tag_admin(self):
        if self.photo:
            return format_html('<img src="{}" width="150" height="150" />'.format(self.photo.url))
        else:
            return 'Hier ist noch kein Bild vorhanden'
    image_tag_admin.short_description = 'Bild'

    def image_tag_png(self):
        if self.photo:
            thumbnail_url = get_thumbnailer(self.photo).get_thumbnail({
                'size': (400, 465),
                'box': self.cropping,
                'crop': True,
                'detail': True,
                }).url
        return format_html('<img src="{}" alt="{}_Rado-Montage" class="img-responsive" />'.format(thumbnail_url,self.name))

    def get_absolute_url(self):
        return reverse('about_app:about_page')

class AboutImg(models.Model):
    title = models.CharField('Titel',max_length=300)
    description = models.TextField('Beschreibung', blank=True, null=True)
    bild = fields.ImageField(upload_to='photo/%m/',blank=True, null=True , dependencies=[FileDependency(attname='bild_png', processor=ImageProcessor(format='PNG', scale={'max_width': 340, 'max_height': 260})),FileDependency(attname='bild_webp', processor=ImageProcessor(format='WEBP', scale={'max_width': 340, 'max_height': 260}))])
    bild_png = fields.ImageField(upload_to='',blank=True, null=True)
    bild_webp = fields.ImageField(upload_to='',blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Überschriften und Hauptfotos"
        verbose_name = "Überschrift und Hauptfoto"



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
        return reverse('about_app:about_page')

class AboutDescription(models.Model):
    title = models.CharField('Titel',max_length=300)
    description = models.TextField('Beschreibung', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Eigenschaften "
        verbose_name = "Eigenschaft"

    def get_absolute_url(self):
        return reverse('about_app:about_page')
