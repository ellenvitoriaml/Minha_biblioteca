import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "minha_biblioteca.settings")
django.setup()

from app.models import Usuario

def set_password():
    usuarios = Usuario.objects.all()

    for usuario in usuarios:
        nova_senha = 'senha_segura'
        usuario.set_password(nova_senha)
        usuario.save()
        print(f"Senha definida para {usuario.email}")

if __name__ == "__main__":
    set_password()