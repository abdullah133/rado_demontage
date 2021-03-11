from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sites.models import Site
from info_app.models import KontaktDatenModel
from .init_listen import kontaktdatenmodel_liste
from .models import HomeSlider, HomeDescription, HomeText, HomeBand, HomeImg

def init_my_db(self):
    obj  = Site.objects.filter(id=1).update(domain='www.rado-demontage.at',name='rado-demontage.at')
    # Init Kontaktdaten
    for el in kontaktdatenmodel_liste.values():
        KontaktDatenModel.objects.update_or_create(
            name=el['name'], website_id=obj, email=el['email'], telefon=el['telefon'], adresse=el['adresse'], ust_idnr=el['ust_idnr'], ort=el['ort'])

    return HttpResponseRedirect("/admin/")

def error_404_view(request, exception):
    return render(request, 'base_app/error_404.html', {}, status=404)


def error_500_view(request):
    return render(request, 'base_app/error_505.html', {}, status=505)

class HomeView(TemplateView):
    template_name = 'base_app/home.html'


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['home_slider'] = HomeSlider.objects.all()
        context['home_descriptions'] = HomeDescription.objects.all()
        context['home_band'] = HomeBand.objects.all()
        context['home_text'] = HomeText.objects.all()
        context['home_img'] = HomeImg.objects.all()
        context['auf_welcher_seite'] = 'home'
        return context

class ImpressumView(TemplateView):
    template_name = 'base_app/impressum.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['auf_welcher_seite'] = 'impressum'


        return context
