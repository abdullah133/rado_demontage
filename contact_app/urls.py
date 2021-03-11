from django.urls import path
from .views import ContactView, ContactViewErfolg

app_name = 'contact_app'

urlpatterns = [

    path('Kontakt/', ContactView.as_view(), name='contact_page'),
    path('Kontakt/Erfolg/', ContactViewErfolg.as_view(), name='contact_erfolg_page'),

]
