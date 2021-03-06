from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def bienvenida(request):
    return render(request, 'landingpage.html')


def players(request):
    jugadores = {'jugadores': Jugador.objects.all()}
    return render(request, 'players.html', jugadores)


def player(request, id):
    jugador = {'jugador': get_object_or_404(Jugador, id=id)}

    return render(request, 'player.html', jugador)


def games(request):
    partidas = {'partidas': Partida.objects.all()}
    return render(request, 'games.html', partidas)