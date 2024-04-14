from django.shortcuts import render, redirect
from .forms import ResForm
from django.contrib.auth.decorators import login_required
from .models import Reservacion


# Create your views here.
def principal(request):
    """"Pagina principal."""
    return render(request, 'gatos/principal.html')

@login_required
def reservaciones(request):
     """Agregar una nueva reservación"""
     if request.method != 'POST':
        form = ResForm()
        print('hola')
     else: 
        form = ResForm(data=request.POST)
        if form.is_valid():
            reservacion = form.save(commit=False)
            reservacion.usuario = request.user
            reservacion.save()
            return redirect('gatos1:confirmacion')
     
     context = {'form': form}
     return render(request, 'gatos/reservaciones.html', context)

def confirmacion(request):
    correo = request.user.email if request.user.is_authenticated else None
    context = {'correo': correo}
    return render(request, 'gatos/confirmacion.html', context)


@login_required
def misreservaciones(request):
    reservaciones = Reservacion.objects.filter(usuario=request.user)
    usuario =  request.user if request.user.is_authenticated else None
    context = {'reservaciones': reservaciones, 'usuario': usuario}
    return render(request, 'gatos/mreserv.html', context)
