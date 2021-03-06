from django.db import models


def image_upload(instance, filename):
    return './users/' + str(instance.id) + '/' + filename


class Jugador(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    pais = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to=image_upload)
    fichas = models.IntegerField()
    partidas = models.ManyToManyField('Partida')

    def __str__(self):
        return f'{self.name} ({self.fichas})'


class Partida(models.Model):
    name = models.CharField(max_length=50)
    fichas_en_juego = models.IntegerField()
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.fichas_en_juego})'
