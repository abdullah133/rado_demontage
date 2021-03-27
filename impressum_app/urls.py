from django.urls import path
from .views import ImpressumView

app_name = 'impressum_app'

urlpatterns = [

    path('Impressum/', ImpressumView.as_view(), name='impressum_page'),


]
