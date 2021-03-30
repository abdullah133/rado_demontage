from django.urls import path
from .views import ProjectDetailView
app_name = 'projects_app'

urlpatterns = [

    path('Projekte/<slug:slug>/<int:pk>/', ProjectDetailView.as_view(), name='projects_detail_page'),


]
