from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Equipamento(models.Model):
    equipamento = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    n_serie = models.CharField(max_length=100)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.equipamento

class OrdemServico(models.Model):
    equipamento = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    n_serie = models.CharField(max_length=100)
    n_os = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    falha = models.CharField(max_length=100)
    graunecessidade = models.CharField(max_length=100)
    datasolicitacao = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.datasoliciatacao = timezone.now()
        self.save()

    def __str__(self):
        return self.nome
        
        
        
