from django.urls import path

from .views import ServiceView

app_name = 'service_app'





urlpatterns = [

    path('Leistungen/', ServiceView.as_view(), name='service_page'),


]
