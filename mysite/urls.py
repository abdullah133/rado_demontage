from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *
from django.views.generic import TemplateView



admin.site.site_header = "Rado-Demontage Admin"
admin.site.index_title = "Rado-Demontage Admin Portal"


sitemaps = {
        'Services':ServicesSitemap,
        'ReferencesText':ReferencesTextSitemap,
        'ReferencesModel':ReferencesModelSitemap,
        'Kategorien':KategorienSitemap,
        'Projects':ProjectsSitemap,
        'AboutDescription':AboutDescriptionSitemap,
    
        'AboutImg':AboutImgSitemap,
        'TeamModel':TeamModelSitemap,
        'HomeSlider':HomeSliderSitemap,
        'KontaktDatenModel':KontaktDatenModelSitemap,
            }


urlpatterns =[
    path('eagle/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="mysite/robots.txt", content_type='text/plain')),
    path('', include('base_app.urls')),
    path('', include('about_app.urls')),
    path('', include('contact_app.urls')),
    path('', include('info_app.urls')),
    path('', include('service_app.urls')),
    path('', include('projects_app.urls')),
    path('', include('references_app.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'base_app.views.error_404_view'
handler500 = 'base_app.views.error_500_view'
