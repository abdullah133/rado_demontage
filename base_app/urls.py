from django.urls import path
from .views import HomeView, init_my_db

app_name = 'base_app'

urlpatterns = [

    path('', HomeView.as_view(), name='home_page'),
    path('init/my/db/', init_my_db, name='init_my_db'),

]
