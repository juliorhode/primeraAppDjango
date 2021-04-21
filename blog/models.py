from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.

# Definimos nuestro modelo
# models.Model le indica a django que es un modelo y el sabra que debe guardarlo en la base de datos
class Post(models.Model):
    # Establecemos relacion entre usuario y autor, y asi si eliminamos el usuario, se elimina lo que haya escrito
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    # este es fecha y hora
    creado = models.DateTimeField(default=timezone.now())
    publicado = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.publicado = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

# https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types