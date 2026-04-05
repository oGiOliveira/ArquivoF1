from django.urls import path 
from myapp import views

#urls do site vem aqui
urlpatterns = [
    path('', views.main, name='mainPage'), 
    path('/Noticias', views.news, name='newsPage'),
    path('/Resultados', views.results, name='resultsPage'),
    path('/Pilotos', views.drivers, name='driversPage'),
    path('/Equipes', views.teams, name='teamsPage'),
    path('/Pistas', views.tracks, name='tracksPage'),
]