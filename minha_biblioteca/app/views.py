from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

def index(request):
     return render ( request , 'index.html' )
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirecionar para a página de login após o registro bem-sucedido
    else:
        form = RegistrationForm()
    return render(request, 'usuarios/registrar_usuario.html', {'form': form})

@login_required
def minha_view_protegida(request):
        return render(request, 'base.html', context)
