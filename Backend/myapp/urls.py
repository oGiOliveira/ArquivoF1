from django.urls import path 
from myapp import views

#urls do site vem aqui
urlpatterns = [
    path('', views.main, name='mainPage'), #pagina principal
    path('inicio', views.main, name='mainPage'), 
    path('noticias', views.news, name='newsPage'),
    path('resultados', views.results, name='resultsPage'),
    path('pilotos', views.drivers, name='driversPage'),
    path('equipes', views.teams, name='teamsPage'),
    path('pistas', views.tracks, name='tracksPage'),
]