from django.urls import path 
from myapp import views

#urls do site vem aqui
urlpatterns = [
    path('', views.mainPage, name='main'), 
]