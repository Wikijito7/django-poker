from django.db import models


class Jugador(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    fichas = models.IntegerField()
    partidas = models.ManyToManyField('Partida')

    def __str__(self):
        return f'{self.name} ({self.fichas})'


class Partida(models.Model):
    name = models.CharField(max_length=50)
    fichas_en_juego = models.IntegerField()

