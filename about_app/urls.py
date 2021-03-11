from django.urls import path
from .views import AboutView

app_name = 'about_app'

urlpatterns = [

    path('ÜberMich/', AboutView.as_view(), name='about_page'),


]
