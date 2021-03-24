from django.db import models
from django.urls import reverse
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
from django.utils.html import format_html
from django.conf import settings
from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageRatioField

class Kategorien(models.Model):
    kategorie_name = models.CharField(max_length=30,blank=True, null=True,)

    def __str__(self):
        return "%s" % (self.kategorie_name)

    class Meta:
        verbose_name_plural = " Kategorien"
        verbose_name = "Kategorie"

    def get_absolute_url(self):
        return reverse('menu_app:menu_page')


class Projects(models.Model):
    kategorie = models.ForeignKey(Kategorien, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=40, blank=False, null=False,)
    bild = fields.ImageField(upload_to='projects/%m/',blank=True, null=True , dependencies=[FileDependency(attname='bild_png', processor=ImageProcessor(format='PNG', scale={'max_width': 340, 'max_height': 260})),FileDependency(attname='bild_webp', processor=ImageProcessor(format='WEBP', scale={'max_width': 340, 'max_height': 260}))])
    bild_png = fields.ImageField(upload_to='projects/%m/',blank=True, null=True)
    bild_webp = fields.ImageField(upload_to='projects/%m/',blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cropping = ImageRatioField('bild', '560x360',)



    def __str__(self):
        return self.title

    def get_cropping_as_list(self):
        if self.cropping:
            return list(map(int, self.cropping.split(',')))


    class Meta:
        verbose_name_plural = "Projekte"
        verbose_name = "Projekt"

    def image_tag_png(self):
        if self.bild:
            thumbnail_url = get_thumbnailer(self.bild_png).get_thumbnail({
                'size': (430, 360),
                'box': self.cropping,
                'crop': True,
                'detail': True,
            }).url

            return format_html('<img src="{}" alt="">'.format(thumbnail_url))
        else:
            return 'Hier ist noch kein Bild vorhanden'
            
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
        print('jaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        png_image_url = self.png_image_url()
        webp_image_url = self.webp_image_url()
        return format_html('<img src="{}" onerror="{}{}{}" class="img-responsive" alt="{}_Webdesinger in Wien" />'.format(webp_image_url,"this.src='",png_image_url,"'",self.title))

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
        return reverse('projects_app:projects_detail_page', kwargs={'pk': self.pk})
