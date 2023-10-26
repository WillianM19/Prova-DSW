from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    sigla_estado = models.CharField(max_length=2)
    
    def __str__(self):
        return self.nome
    
    
class Curso(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    data_de_nascimento = models.DateField()
    
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
