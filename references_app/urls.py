from django.urls import path
from .views import ReferencesView

app_name = 'references_app'

urlpatterns = [

    path('Referenzen/', ReferencesView.as_view(), name='references_page'),
]
