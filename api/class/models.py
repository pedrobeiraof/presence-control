from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    foto = models.ImageField()
    is_presente = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Aula(models.Model):
    ds_aula = models.CharField(max_length=30)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.ds_aula