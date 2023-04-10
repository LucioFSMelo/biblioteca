from django.db import models
from datetime import date

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.nome

class Livros(models.Model):

    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=40)
    editora = models.CharField(max_length=30)
    data_cadastro = models.DateField(default= date.today)
    edicao = models.CharField(max_length=30)
    ano_edicao = models.CharField(max_length=50)
    emprestado = models.BooleanField(default=False)
    description = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete= models.DO_NOTHING)
    

    class Meta:
        verbose_name = 'Livro'
        
    def __str__(self):
        return self.titulo

