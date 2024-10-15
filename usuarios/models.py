from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Usuarios(models.Model):
    # Define o campo nome como uma string com no máximo 50 caracteres
    nome = models.CharField(max_length=50)
    
    # Define o campo idade como um número inteiro, com validação para valores entre 0 e 150
    idade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    
    # Define o campo email como um endereço de e-mail único, com valor padrão e anulável
    email = models.EmailField(max_length=254, null=True, blank=True)  # Campo email como anulável
    
    # Define o campo profissão como uma string com no máximo 100 caracteres, com valor padrão e anulável
    profissao = models.CharField(max_length=100, null=True, blank=True)  # Campo profissao como anulável
    
    # Define o campo mensagem como um texto com possibilidade de ser vazio
    mensagem = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        # Retorna o nome do usuário quando o objeto é convertido para string
        return self.nome
