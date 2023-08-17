from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    posicion = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"
    
        class Meta:
            verbose_name = "Jugador"
            verbose_name_plural = "Jugadores"

class Tecnico(models.Model):
    nombre = models.CharField(max_length=50)
    estilo = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tecnico"
        verbose_name_plural = "Tecnicos"

    def __str__(self):
        return f"{self.nombre}"
    
class Formacion(models.Model):
    formacio = models.CharField(max_length=50)
    tactica = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Formación"
        verbose_name_plural = "Formaciones"

    def __str__(self):
        return f"{self.formacio} {self.tactica}"
