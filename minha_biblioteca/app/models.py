from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from app.utils import proximo_valor_sequencia


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo de email deve ser preenchido.')
        email = self.normalize_email(email)
        user = self.model(email=email, nickname=nickname, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nickname, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, default='example@example.com')
    nickname = models.CharField(max_length=30, unique=True, default='usuario_padrao')
    password = models.CharField(max_length=128, default='')
    nome = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.password:
            self.password = make_password(self.password)
        super().save(*args,**kwargs)
    
    class Meta:
        db_table = "usuario"
    
class Biblioteca(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "bibliotecas"

class Editora(models.Model):
    editora_id = models.AutoField(primary_key=True, default=proximo_valor_sequencia)
    nome = models.CharField(max_length=255)
    localizacao = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.Nome
    
    class Meta:
        db_table = "editora"

class Genero(models.Model):
    Nome = models.CharField(max_length=255)

    def __str__(self):
        return self.Nome
    
    class Meta:
        db_table = "genero"

class StatusLivro(models.Model):
    Nome = models.CharField(max_length=20)

    def __str__(self):
        return self.Nome

class Livro(models.Model):
    Titulo = models.CharField(max_length=255)
    Ano_Publicacao = models.IntegerField(blank=True, null=True)
    Status_ID = models.ForeignKey(StatusLivro, on_delete=models.CASCADE)
    Sinopse = models.TextField(blank=True, null=True)
    Editora_ID = models.ForeignKey(Editora, on_delete=models.CASCADE)

    def __str__(self):
        return self.Titulo

class Autor(models.Model):
    Nome = models.CharField(max_length=255)
    Nacionalidade = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Nome

class Exemplar(models.Model):
    Numero = models.IntegerField()
    Disponibilidade = models.BooleanField(default=True)
    Livro_ID = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return f"Exemplar {self.Numero} de {self.Livro_ID}"

class Emprestimo(models.Model):
    Data_Emprestimo = models.DateField()
    Data_Devolucao = models.DateField(blank=True, null=True)
    Usuario_ID = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Empréstimo para {self.Usuario_ID}"

class Avaliacao(models.Model):
    Nota = models.IntegerField()
    Comentario = models.TextField(blank=True, null=True)
    Usuario_ID = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Livro_ID = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return f"Avaliação de {self.Livro_ID} por {self.Usuario_ID}"

class ListaDesejos(models.Model):
    Usuario_ID = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Livro_ID = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return f"Lista de Desejos de {self.Usuario_ID}"

class Proprietario(models.Model):
    Nome = models.CharField(max_length=255)
    Endereco = models.CharField(max_length=255, blank=True, null=True)
    Email = models.CharField(max_length=255)

    def __str__(self):
        return self.Nome

class Emprestimo_Exemplar(models.Model):
    Emprestimo_ID = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    Exemplar_ID = models.ForeignKey(Exemplar, on_delete=models.CASCADE)

    def __str__(self):
        return f"Empréstimo {self.Emprestimo_ID} - Exemplar {self.Exemplar_ID}"

class Emprestimo_Usuario(models.Model):
    Emprestimo_ID = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    Usuario_ID = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Empréstimo {self.Emprestimo_ID} - Usuário {self.Usuario_ID}"
