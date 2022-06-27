from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)


class Curso(models.Model):
    nome_do_curso = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    inicio = models.DateField()
    termino = models.DateField()
    professor = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'groups__name':'Professores'}, related_name="Professor")
    student = models.ManyToManyField(CustomUser, limit_choices_to={'groups__name': 'Alunos'}, blank=True)

    def __str__(self):
        return self.nome_do_curso

