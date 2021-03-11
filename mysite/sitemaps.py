from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from contact_app.models import ContactInfo
from about_app.models import AboutContent

class AboutContentSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return AboutContent.objects.all()

class ContactInfoSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return ContactInfo.objects.all()
