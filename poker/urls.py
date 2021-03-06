from django.contrib import admin
from django.urls import include, path

from poker import views

urlpatterns = [
    path('', views.bienvenida),
    path('jugadores/', views.players),
    path('jugador/<int:id>', views.player),
    path('partidas/', views.games)
]
