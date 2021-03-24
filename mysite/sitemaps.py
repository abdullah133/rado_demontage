from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from about_app.models import AboutDescription, AboutImg, TeamModel
from base_app.models import HomeSlider
from info_app.models import KontaktDatenModel
from projects_app.models import Projects, Kategorien
from references_app.models import ReferencesModel, ReferencesText
from service_app.models import Services

class ServicesSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Services.objects.all()

class ReferencesTextSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return ReferencesText.objects.all()

class ReferencesModelSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return ReferencesModel.objects.all()

class KategorienSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Kategorien.objects.all()

class ProjectsSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Projects.objects.all()

class AboutDescriptionSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return AboutDescription.objects.all()

class AboutImgSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return AboutImg.objects.all()

class TeamModelSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return TeamModel.objects.all()

class HomeSliderSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return HomeSlider.objects.all()

class KontaktDatenModelSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return KontaktDatenModel.objects.all()
