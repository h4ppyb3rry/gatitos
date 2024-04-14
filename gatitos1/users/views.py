from django.shortcuts import render, redirect 
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import RegistroForm

# Create your views here.

def register(request):
    """Registrar un nuevo usuario"""
    if request.method != 'POST':
        form = RegistroForm()
    else:
        form = RegistroForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('gatos1:principal')
    #Despliega un formulario en blanco o inválido
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def logoutt(request):
    logout(request)
    return render(request, 'registration/logged_out.html')